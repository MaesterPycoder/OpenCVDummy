import cv2
# playing video

capture = cv2.VideoCapture(r'C:\Users\S.S Shanmukkha\Desktop\dumvid.mp4')
while True:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Reached the end of the video')
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(30)
    if key == 27:
        print('Pressed Esc')
        break
cv2.destroyAllWindows()