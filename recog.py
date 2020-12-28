import cv2
import numpy as np

# img = cv2.imread(r"C:\Users\S.S Shanmukkha\Desktop\test.jpeg")
img = cv2.imread('MyPhoto/shanmukkha.jpg')
gm = 2.0

cor_img = np.power(img, gm)
cv2.imshow('Original_image', img)
cv2.imshow('Corrected_image',cor_img)
cv2.waitKey(0)
cv2.destroyAllWindows()