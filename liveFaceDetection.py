import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    has_frame, img = cap.read()
    if not has_frame:
        print(r'Can\'t get frame')
        break
    # img = frame
    # img = cv2.imread(frame)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('img', img)
    key = cv2.waitKey(40)
    if key == 27:
        print('Pressed Esc')
        break

cv2.destroyAllWindows()
cap.release()
