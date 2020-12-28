# Capturing Video using openCV

import cv2

cap = cv2.VideoCapture(0)
while True:
    has_frame, frame = cap.read()
    if not has_frame:
        print('Can\'t get frame')
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed Esc')
        break
cap.release()
cv2.destroyAllWindows()