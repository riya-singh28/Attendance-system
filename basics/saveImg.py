import cv2
import os
directory = 'cascades/dataset/User'
os.chdir(directory)

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

videoCaptureObject = cv2.VideoCapture(0)
result = True
count = 0
while(result):
    ret,frame = videoCaptureObject.read()
    #cv2.imwrite("NewPicture.jpg",frame)
    cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", frame)
    cv2.imshow('image', frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()