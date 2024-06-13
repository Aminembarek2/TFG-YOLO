# keep coordinates and keep 'Car', 'Pedestrian', 'Cyclist'
import os

# Directory containing the label files
label_dir = "kitti/train"

# Function to parse label lines and extract required information
def parse_label_line(line):
    parts = line.split()
    if len(parts) >= 15:
        object_type = parts[0]
        if object_type in ['Car', 'Pedestrian', 'Cyclist']:
            left, top, right, bottom = map(float, parts[4:8])
            return f"{object_type} {left} {top} {right} {bottom}\n"
    return None

# Function to process label files
def process_label_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        parsed_lines = [parse_label_line(line) for line in lines]
    
    # Remove None values and write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines([line for line in parsed_lines if line])

# Iterate over label files in the directory
for file_name in os.listdir(label_dir):
    if file_name.endswith(".txt"):
        file_path = os.path.join(label_dir, file_name)
        print(f"Processing file: {file_path}")
        process_label_file(file_path)