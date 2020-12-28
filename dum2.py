
# Histogram plot

import matplotlib.pyplot as plt
import cv2
import numpy as np

grey = cv2.imread(r"C:\Users\S.S Shanmukkha\PycharmProjects\FaceRecog\MyPhoto\index.jpg")
cv2.imshow('original grey', grey)
cv2.waitKey()
cv2.destroyAllWindows()
hist, bins = np.histogram(grey, 256, [0, 255])
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()

