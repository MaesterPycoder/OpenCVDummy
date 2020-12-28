import cv2
import numpy as np
import matplotlib.pyplot as plt
# image = cv2.imread(r'C:\Users\S.S Shanmukkha\Pictures\My Photos\profile.jpg').astype(np.float32) / 255

image = cv2.imread(r'C:\Users\S.S Shanmukkha\Desktop\test.jpeg').astype(np.float32) / 255

noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0, 1)
plt.imshow(noised[:,:,[2,1,0]])
plt.show()

gauss_blur = cv2.GaussianBlur(noised, (7, 7), 0)
plt.imshow(gauss_blur[:, :, [2, 1, 0]])
plt.show()
