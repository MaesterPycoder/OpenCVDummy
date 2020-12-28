import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path = "MyPhoto"

img = cv.imread(f"MyPhoto/index.jpg", 1) # color image
gimg = cv.imread(f"MyPhoto/index.jpg", 0) # grey image



# resize_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
#
# print(gimg.shape)
# print(img.shape)
# cv.imshow("color", resize_img)
cv.imshow("grey", gimg)
# hist, bins = np.histogram(img, 256, [0, 255])
# plt.fill(hist)
# plt.xlabel('pixel value')
# plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
