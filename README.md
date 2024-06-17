# TFG-YOLO

## Overview
This project is based on the YOLO (You Only Look Once) algorithm for object detection. It includes scripts for training, testing, and preparing KITTI dataset.

## Directory Structure
- `DatasetPreparation`: Contains scripts for preparing datasets.
  - `keep_ness.py`
  - `map.py`
  - `normalization.py`
- `devkit_object-3`: Contains scripts and data for evaluation and mapping.
- `train.py`: Script for training the YOLO model.
- `test.py`: Script for testing the YOLO model.
- `data.yaml`: Configuration file for the dataset.
- `trainlist.txt`: List of training data files.
- `testlist.txt`: List of testing data files.

## Getting Started

### Prerequisites
- Python 3.x
- Install ```pip install ultralytics```
## Usage
### Dataset Preparation

Prepare your dataset using the scripts in the DatasetPreparation directory. For example:
```python DatasetPreparation/keep_ness.py```
### Training
Train the YOLO model using the train.py script:
```python train.py```
### Testing
To generate the test results of the model using the test.py script:
```python test.py```
### Model Evaluation
To evaluate the model, use the evaluation kit. You need to reverse the normalization and change the labels first. For missing values (occlusion, 3D coordinates, etc.), insert the ignored values (e.g., -1, -10). Check [this link](https://github.com/cguindel/eval_kitti) for more information on how to test using the KITTI evaluation kit.
