from ultralytics import YOLO
model = YOLO('Cat_Dog_Detection/runs/detect/nanoModel2/weights/best.pt')  # load a custom best model

# Validate the model
metrics = model.val(plots=True,conf=0.4,data="Cat_Dog_Detection/config.yaml")  
