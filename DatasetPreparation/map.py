import os

# Directory containing the modified label files
label_dir = "kitti/train/labels"

# Mapping of object types
label_mapping = {
    "Car": "0",
    "Pedestrian": "1",
    "Cyclist": "2",
}

# Function to update label files with the new mapping
def update_label_files(label_dir):
    for file_name in os.listdir(label_dir):
        if file_name.endswith(".txt"):
            file_path = os.path.join(label_dir, file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            with open(file_path, 'w') as file:
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 1:
                        object_type = parts[0]
                        if object_type in label_mapping:
                            parts[0] = label_mapping[object_type]
                            updated_line = ' '.join(parts) + '\n'
                            file.write(updated_line)
                        else:
                            file.write(line)

# Update label files with the new mapping
update_label_files(label_dir)

print("Labels updated successfully.")