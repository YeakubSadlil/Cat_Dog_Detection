<h1 align="center">Cat and Dog Detection using YOLOv8</h1>

<p align="center">
  <img src="https://img.shields.io/badge/made%20by-YeakubSadlil-blue.svg" >
  <img src="https://img.shields.io/badge/YOLOv8-orange.svg">
  <img src="https://img.shields.io/badge/python-3.8-blue.svg">
</p>

<p align="center">
  <img src="https://github.com/YeakubSadlil/Cat_Dog_Detection/blob/master/runs/detect/nanoModel2/predict/images27.jpg" width="50%">
</p>

## Table of Contents
* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [How to Use the Model](#How-to-Use-the-Model)
* [Preprocessing](#Preprocessing)
* [Training and Modeling](#Training-and-Modeling)
* [Evaluation](#Evaluation)
* [Model Deployment with Flask Api](#Model-Deployment-with-Flask-Api)
* [Results](#Results)
* [Conclusion](#Conclusion)


## About The Project
This project aims to detect cats and dogs in images using the YOLOv8 algorithm. It was trained on a dataset of 103 annotated cat and dog images and achieved an F1-score of 0.92.

### Why YOLOv8 ?
YOLOv8 is a highly efficient and accurate object detection system that is well-suited for real-time object detection applications<br>
and itis the latest version of the YOLO series. Its combination of a ResNet-50 backbone, Mosaic data augmentation.<br>
YOLOv8 outperforms all previous YOLO models.

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
* Python 3.8
* YOLOv8
* ultralytics
* torch>=1.7.0
* Flask
* OpenCV
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/YeakubSadlil/Cat_Dog_Detection.git 
   
## How to Use the Model?
* Simply navigate to the direcory 'FlaskApi'
* Run the python file 'app.py'.
* Go to the link on your browser http://127.0.0.1:5000/
* It will show you an user interface to upload image.
* Upload and wait, you will get your annotated image.

### Preprocessing
I've annotated 103 images to yolo format using <a href="https://www.cvat.ai/">CVAT.ai</a>.The images with no objects are annotated as 0.<br>
So that false positive will be reduced. There was an image with .svg<br> format. I've converted it .jpg to feed YOLO model.

### Training and Modeling
A pretrained nano YOLOv8 model is used with 150 epochs with augmentation like as mosaic=1.0,hsv_h=0.015.<br>
I've tried with different YOLOv8 model like as small,medium and large versions.But nano performed better.<br>
After using data augmentation overfitting is slightly reduced.<br>
I've tried with different optimizers,learning rates,batch size but SGD performed better with default learning rate.

### Evaluation
<p align="center">
  <img src="https://github.com/YeakubSadlil/Cat_Dog_Detection/blob/master/runs/detect/nanoModel2/results.png" width="50%">
</p>
It seems like the model is slightly overfitted by observing Val/Box loss.I think the reason is smaller dataset.<br>
The model isn't improving after 100 epochs.
</p>
<p align="center">
  <img src="https://github.com/YeakubSadlil/Cat_Dog_Detection/blob/master/runs/detect/nanoModel2/F1_curve.png" width="50%">
</p>
The f1-confidence curve shows the performance of your YOLO model for each class at different confidence thresholds.<br>
In this case, the curve is showing an f1 score of 0.92 for all classes when the confidence threshold is set to 0.486.<br>
This means that your model is performing well for all the classes at this threshold, with a good balance of precision and recall.
That's why I set confidence threshold near to 0.48 during predicting images and yields better predictions.

</p>
<p align="center">
  <img src="https://github.com/YeakubSadlil/Cat_Dog_Detection/blob/master/runs/detect/nanoModel2/PR_curve.png" width="50%">
</p>

The precision is 0.955 at a mean average precision (mAP) of 0.5. This means that the classifier has a high level of accuracy<br>
in identifying positives and negatives, and the predicted positives are mostly true positives. A high mAP of 0.5 indicates that<br>
the classifier is performing well across all classes.

</p>
<p align="center">
  <img src="https://github.com/YeakubSadlil/Cat_Dog_Detection/blob/master/runs/detect/nanoModel2/confusion_matrix.png" width="50%">
</p>

92% times cats and dogs are correctly identified when they were actually cats and dogs.

## Model Deployment with Flask Api
This is a Python Flask web application that allows users to upload an image file (PNG, JPG, JPEG).<br>
Once an image is uploaded, the application performs object detection on the image using a function<br>
called bounding_image defined in the file image_detection.py. The detected objects are then annotated<br>
with bounding boxes and the annotated image is returned as the response to the user's request.<br>

The allowed_file function checks if the uploaded file is a valid image file. If the file is invalid or<br>
not present, the application returns an error message.<br>

The HTML template displays a simple upload form for the user to select an image file and submit it to the server.<br>
## Results
</p>
<p align="centre">
  <img src="https://github.com/YeakubSadlil/Cat_Dog_Detection/blob/master/Cat_dog_data/images/test/pexels-photo-4214919.jpeg" height="40%" width="30%">

<img align="centre">
  <img src="https://github.com/YeakubSadlil/Cat_Dog_Detection/blob/master/runs/detect/nanoModel2/predict/pexels-photo-4214919.jpeg" height="40%" width="30%">

## Conclusion
This project demonstrates the effectiveness of YOLOv8 for object detection in small datasets. With further training and optimization<br> with large data set the model can be improved to achieve even higher accuracy and performance
