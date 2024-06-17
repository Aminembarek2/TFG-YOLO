from ultralytics import YOLO,settings
import os

# Load a model (the Url is not correct)
model = YOLO(f'/home/kitti/best.pt')

# Evaluate the model's performance on the test set
metrics = model.val(split="test", save_txt=True, save_conf=True)

