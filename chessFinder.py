import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(2)

# Automatically grab width and height from video feed
# (returns float which we need to convert to integer for later on!)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:

    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    
    found, corners = cv2.findChessboardCorners(gray,(7,7))

    if found:
        print("found corners")


        board = gray.copy()
        cv2.drawChessboardCorners(board,(7,7), corners, found)
        cv2.imshow('board',board)

    else:
        print("unable to see corners")

    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
