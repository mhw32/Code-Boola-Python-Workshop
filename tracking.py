# -------------------
# Code Boola 2016
# Python Workshop
# Tracking eyes & face
# -------------------

import cv2
import sys

faceCascPath = './haarcascade_frontalface_default.xml'
eyeCascPath = './haarcascade_eye.xml'
faceCascade = cv2.CascadeClassifier(faceCascPath)
eyeCascade  = cv2.CascadeClassifier(eyeCascPath)
video_capture = cv2.VideoCapture(0)

while True:
  # Capture frame-by-frame
  ret, frame = video_capture.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
  )

  # Draw a rectangle around the faces
  for (x, y, w, h) in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    # Draw for eyes as well.
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    eyes = eyeCascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

  # Display the resulting frame
  cv2.imshow('Video', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()