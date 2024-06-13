import os
import cv2

# Paths to directories
images_dir = "kitti/train/images"
labels_dir = "kitti/train/labels"

# Function to normalize coordinates
def normalize_coordinates(xmin, ymin, xmax, ymax, image_width, image_height):
    x_center = (xmin + xmax) / 2
    y_center = (ymin + ymax) / 2
    width = xmax - xmin
    height = ymax - ymin
    
    x_center_normalized = x_center / image_width
    y_center_normalized = y_center / image_height
    width_normalized = width / image_width
    height_normalized = height / image_height
    
    return x_center_normalized, y_center_normalized, width_normalized, height_normalized

# Iterate over label files and find corresponding images
for label_name in os.listdir(labels_dir):
    if label_name.endswith(".txt"):
        label_path = os.path.join(labels_dir, label_name)
        image_name = label_name[:-4] + ".png"  # Change to .png if different
        image_path = os.path.join(images_dir, image_name)

        # Check if image file exists to prevent errors
        if os.path.exists(image_path):
            # Read the image to get its dimensions
            image = cv2.imread(image_path)
            if image is not None:
                image_height, image_width, _ = image.shape

                # Read the label file, normalize the coordinates, and rewrite the file with normalized coordinates
                with open(label_path, 'r') as label_file:
                    lines = label_file.readlines()
                
                with open(label_path, 'w') as label_file:
                    for line in lines:
                        class_id, xmin, ymin, xmax, ymax = map(float, line.split())
                        x_normalized, y_normalized, w_normalized, h_normalized = normalize_coordinates(
                            xmin, ymin, xmax, ymax, image_width, image_height
                        )
                        # Write the normalized coordinates back into the label file
                        label_file.write(f"{int(class_id)} {x_normalized} {y_normalized} {w_normalized} {h_normalized}\n")

