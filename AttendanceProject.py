import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

from PIL import ImageGrab

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        encodeList.append(encode)
    return encodeList


#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
def captureScreen(bbox=(300,300,690+300,530+300)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    facesCurFrame = face_recognition.face_locations(capScr)
    encodesCurFrame = face_recognition.face_encodings(capScr, facesCurFrame)
    return capScr
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)

encodeListKnown = findEncodings(images)
print('Encoding Complete')







