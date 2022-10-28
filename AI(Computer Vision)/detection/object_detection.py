import picamera
import time
import cv2
import tensorflow as tf
import numpy as np

# Yolov3-tiny model load
net = cv2.dnn.readNet("/yolov3-tiny.weights", "/darknet/cfg/yolov3-tiny.cfg")
classes = []
with open("darknet/data/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

cap = cv2.VideoCapture(-1) # 0, 1, 2 순서로 연결된 카메라 인덱스번호, 오류발생시 -1 넣어주기

fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')
#movie = cv2.VideoWriter('detection.mpeg4', fourcc, 20.0, (640,480)) # fps, size

while(cap.isOpened()): # 카메라 켜져있을 때 반복실행
  ret, frame = cap.read() # 프레임 하나 읽고 값 반환 (ret은 boolean, frame은 사진이 배열로 들어감)
  
  if(ret):
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392,(640,480), (0,0,0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # confidence가 0.5 이상이면 해당 Object라고 탐지
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
      for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
          center_x = int(detection[0] * width)
          center_y = int(detection[1] * height)
          w = int(detection[2] * width)
          h = int(detection[3] * height)            
          x = int(center_x - w / 2)
          y = int(center_y - h / 2)
          boxes.append([x, y, w, h])
          confidences.append(float(confidence))
          class_ids.append(class_id)

    # 박스 중복을 방지하기 위해 noise를 지워주는 과정
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
      if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label+' '+str(confidences[i]), (x, y + 30), font, 1, color, 2)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1) & 0xFF
    if(k==27):
      break




cap.release()
cv2.destroyAllWindows()