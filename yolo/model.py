from ultralytics import YOLO
import cv2

model = YOLO("../Yolo-weights/yolov8l.pt")

result = model("object3.png", show=True)
cv2.waitKey(0)
