from ultralytics import YOLO
import os

# Load a pretrained YOLO model
model = YOLO('yolov8x.pt')

model.train(data='/home/kitti/data.yaml', project="models",epochs=40, save=True, imgsz=640, device='0', val=False, mosaic=0.0,save_period=10, lrf=0.0001, lr0=0.0001, batch=32)