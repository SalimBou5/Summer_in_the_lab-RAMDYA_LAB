import sys
import cv2

port = 0
rec = False
# Open a connection to the webcam (camera index 0 by default)
cap = cv2.VideoCapture(port)

cont = 0

# Check if the camera opened successfully
while cap.isOpened():
    # Capture frame-by-frame    
    ret, frame = cap.read()
    imgS = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # set green and red channels to 0
    imgS[:, :, 1] = 0

    imgR = cv2.cvtColor(imgS, cv2.COLOR_HSV2BGR)
    if ret:
        if cv2.waitKey(1) == ord('r'):
            rec = not rec
        if rec:
            imgR = cv2.resize(imgR,(760,570))
        # Display the frame
        cv2.imshow('Camera Feed', imgR)
    else:
        break

# Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()