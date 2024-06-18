import os
from PIL import Image

# Define the model name
model_name = 'model_ep10'

# Function to get image dimensions
def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

# Function to reverse normalization
def reverse_normalization(class_id, x_center_normalized, y_center_normalized, width_normalized, height_normalized, image_width, image_height):
    class_map = {0: 'Car', 1: 'Pedestrian', 2: 'Cyclist'}
    class_name = class_map[class_id]
    width = width_normalized * image_width
    height = height_normalized * image_height
    x_center = x_center_normalized * image_width
    y_center = y_center_normalized * image_height
    xmin = x_center - width / 2
    xmax = x_center + width / 2
    ymin = y_center - height / 2
    ymax = y_center + height / 2
    return class_name, xmin, ymin, xmax, ymax

# Ensure output directory exists
output_directory = f"final_runs/{model_name}" #
os.makedirs(output_directory, exist_ok=True)

# Process the model name
label_directory = f"final_runs/{model_name}/labels"
image_directory = "finaldataset/test/images"

# Iterate over label files in the directory
for label_file in os.listdir(label_directory):
    if label_file.endswith(".txt"):  # Adjust the extension based on your files
        label_path = os.path.join(label_directory, label_file)
        output_path = os.path.join(output_directory, label_file)  # Output to the same filename in a different directory
        image_filename = label_file.replace(".txt", ".png")  # Assuming the image has the same name but different extension
        image_path = os.path.join(image_directory, image_filename)
        image_width, image_height = get_image_dimensions(image_path)

        with open(label_path, 'r') as file, open(output_path, 'w') as output_file:
            for line in file:
                parts = line.strip().split()
                class_id = int(parts[0])
                coords = list(map(float, parts[1:5]))
                conf = float(parts[-1])
                class_name, xmin, ymin, xmax, ymax = reverse_normalization(class_id, *coords, image_width, image_height)
                output_file.write(f"{class_name} {xmin:.2f} {ymin:.2f} {xmax:.2f} {ymax:.2f} {conf:.2f}\n")

######### Keep #########
directory = f'final_runs/{model_name}'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    # Only process files (skip directories)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Filter lines based on the last value
        filtered_lines = [line for line in lines if float(line.split()[-1]) > 0.15]
        
        # Write the filtered lines back to the same file
        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)

print("Processing complete.")

########### Fill ###########
def fill_missing_data(input_dir, secondary_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over all files in the input directory
    for file_name in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, file_name)
        secondary_file_path = os.path.join(secondary_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)

        # Check if the secondary file exists
        if not os.path.isfile(secondary_file_path):
            print(f"Warning: No matching file in secondary directory for {file_name}")
            continue  # Skip processing this file if the secondary file does not exist

        # Open the input file, secondary file, and create a new output file
        with open(input_file_path, 'r') as input_file, open(secondary_file_path, 'r') as secondary_file, open(output_file_path, 'w') as output_file:
            # Read lines from both files
            input_lines = input_file.readlines()
            secondary_lines = secondary_file.readlines()

            # Process each line from the input file along with the corresponding line from the secondary file
            for input_line, secondary_line in zip(input_lines, secondary_lines):
                parts_input = input_line.strip().split()
                parts_secondary = secondary_line.strip().split()

                type_of_object = parts_input[0]
                # Replace with values from the secondary file
                x1, y1, x2, y2, conf = parts_input[1], parts_input[2], parts_input[3], parts_input[4], float(parts_input[5])
                o, t, a = parts_secondary[1], parts_secondary[2], parts_secondary[3]
                # Format the output line using values from the secondary file
                output_line = f"{type_of_object} -1 -1 -10 {x1} {y1} {x2} {y2} -1 -1 -1 -1000 -1000 -1000 -10 {conf}\n"
                output_file.write(output_line)

# Specify the input directory containing the label files, the secondary directory with updated values, and the output directory to save the modified labels
input_dir = f'final_runs/{model_name}'
secondary_dir = 'eval_kitti/build/data/object/label_2'
output_dir = f'eval_kitti/build/results/exp_runs{model_name}_0.0/data'
os.makedirs(output_dir, exist_ok=True)
fill_missing_data(input_dir, secondary_dir, output_dir)

print(f"Processing for {model_name} complete.")

def list_txt_files(directory, output_file):
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Filter out only .txt files
    txt_files = [f for f in files if f.endswith('.txt')]
    
    # Write the list of .txt files to the output file
    with open(output_file, 'w') as file:
        for txt_file in txt_files:
            file.write(txt_file + '\n')

# Define the directory and the output file
directory = f'eval_kitti/build/results/exp_runs_{model_name}/data'
output_file = f'eval_kitti/build/lists/exp_runs_{model_name}.txt'

# Call the function to list .txt files
list_txt_files(directory, output_file)
