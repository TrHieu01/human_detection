# -*- coding: utf-8 -*-
"""yolov11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EObGirxmHqCJ5w0_l2v6eTpnMPTpVEcz
"""

! git clone https://github.com/ultralytics/ultralytics.git

! pip install ultralytics

import ultralytics
ultralytics.checks()

! wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11s.pt

! gdown 1--0QuKMwj31K-CSvD8oq5fceFweiFPuN

! unzip /content/human_detection_dataset.zip

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/ultralytics

!mv ../human_detection_dataset .

import yaml
import os

dataset_infor = {
    'train':'./train/images',
    'val':'./val/images',
    'path': '/content/ultralytics/human_detection_dataset',
    'nc': 1,
    'name':['Human']
}


yaml_filepath = './human_detection_dataset/data.yaml'
with open(yaml_filepath, 'w') as file:
    doc = yaml.dump(dataset_infor,
                    file,
                    default_flow_style=None,
                    sort_keys=False)

!yolo train model=/content/yolo11s.pt  data=./human_detection_dataset/data.yaml epochs =50 imgsz=640

!yolo predict model=/content/ultralytics/runs/detect/train/weights/best.pt source='https://img.tripi.vn/cdn-cgi/image/width=700,height=700/https://gcs.tripi.vn/public-tripi/tripi-feed/img/474082GDs/hinh-anh-chup-nhom-3-nguoi-dep_012942018.jpg'