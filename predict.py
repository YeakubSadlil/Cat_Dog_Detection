from ultralytics import YOLO
from PIL import Image

model = YOLO("Cat_Dog_Detection/runs/detect/nanoModel2/weights/best.pt")
# predict all test images
results = model.predict(source="Cat_Dog_Detection/Cat_dog_data/images/test", save=True,conf=0.4) 

#predict a video
#results = model.predict(source="Cat_Dog_Detection/Cat_dog_data/cat_dog.webm", save=True,conf=0.4)


# from PIL
# im1 = Image.open("Data/images/train/images22.jpg")
# results = model.predict(source=im1, save=True,save_conf=True) 
