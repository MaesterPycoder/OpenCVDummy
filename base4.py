import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('MyPhoto/shanmukkha.jpg')
img = cv2.imread(r"C:\Users\S.S Shanmukkha\Desktop\test.jpeg")
rimg = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 2))
gimg = cv2.cv2.cvtColor(rimg, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gimg, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(gimg, (x, y), (x + w, y + h), (0, 255, 0), 2, 1, None)
cv2.imshow("Image", gimg)
cv2.waitKey(0)
