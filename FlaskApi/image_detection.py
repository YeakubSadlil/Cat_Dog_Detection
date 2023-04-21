import cv2
import math
from ultralytics import YOLO

def bounding_image(path):
    img =cv2.imread(path)

    model = YOLO('best.pt')  # Best trained model
    classNames = ["cat", "dog"]

    results = model(img)
    for i in results:
        boxes = i.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            print(x1,y1,x2,y2)
            cv2.rectangle(img,(x1,y1),(x2,y2),(220,45,60),3)
            conf = math.ceil(box.conf[0]*100)/100
            cls=int(box.cls[0])
            class_name=classNames[cls]
            label=f'{class_name}-{conf}'
            text_size = cv2.getTextSize(label,0,fontScale=1,thickness=2)[0]
            c2 = x1+text_size[0],y1-text_size[1]-3
            cv2.rectangle(img,(x1,y1),c2,(25,245,54),-1,cv2.LINE_AA)
            cv2.putText(img,label,(x1,y1-3),0,1,(0,0,255))
    return img