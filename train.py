from ultralytics import YOLO
model = YOLO("yolov8n.pt") 
model.train(data="Cat_dog_detector/config.yaml", epochs=150,imgsz=640,batch=8,patience=40,name='nanoModel2',hsv_h=0.015,hsv_s=0.5,hsv_v=0.3,degrees=0.0,translate=0.1,scale=0.2,shear=1.0,flipud=0.5,fliplr=0.5,mosaic=1.0,mixup=0.1)