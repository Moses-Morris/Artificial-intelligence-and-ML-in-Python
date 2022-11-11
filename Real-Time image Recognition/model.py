import numpy as np #math A 21 > 6
import imutils #resize the image
import cv2 #image acq.
import time #delay
prototxt = "Mobile NetSSD_deploy.prototxt.txt"
model = "Mobile NetSSD_deploy.caffemodel"
confThresh = 0.2
CLASSES =  [" background", "aeroplane" , "bicycle" , "bird", "boat",
"bottle", "bus", "car" , "cat" , "chair" , "cow" , "diningtable",
"dog", "horse", "motorbike" , "person", "pottedplant", "sheep",
"sofa" , "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("Loading model ...")
net = cv2.dnn.readNetFromCaffe(prototxt, model)
print("Model Loaded")
pint("Starting Camera Feed ...")
vs = cv2.VideoCapture(1)
time.sleep(2.0)
while True:
        _frame = vs.read()
        frame = imutils.resize(frame, width=500)
        (h, w) = frame.shape[:2]
        imResize = cv2.resize(frame, (300, 300))
        blob = cv2.dnn.blobFromImage(imResize,
        0.007843, (300, 300), 127.5)

   
        net.setInput(blob) #set the blobbed image as
        ww
        detections = net.forward() #passing pre processed image into

        detShape = detections.shape[2]
        for i in np.arange(0,detShape):
            confidence = detections[0, 0, i, 2]
       
            if confidence > confThresh:
                idx = int(detections[0, 0, i, 1])
                print("ClassID:", detections[0, 0, 1, 1])
                box = detections[0, 0, i, 3 :7] * np.array([w , h , w,
                print("boxCoord:", detections[0, 0, 1, 3 :7])
                (startX, startY, endX, endY) =  box.astype("int")

                label = "{}: {: .2f}%" . format(CLASSES[idx], confidence * 100)
                cv2.rectangle(frame, (startX, startY) , (endX, endY), COLORS[idx], 2)
                if starty - 15 > 15:
                y = starty - 15
                else:
                y = starty + 15
                cv2.putText(frame, label, (startx, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS [idx], 2)

                cv2.putText(frame, label, (startx, y),
                cv2.FONT main
frame: Any = (vs.read())[1]
show("Frame", frame)
cv2.waitkey(1)
== 27:
eak
()
yAllWindows()