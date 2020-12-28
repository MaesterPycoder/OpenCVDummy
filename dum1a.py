import numpy as np
import cv2
import matplotlib.pyplot as plt

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

original = cv2.imread(r"C:\Users\S.S Shanmukkha\PycharmProjects\FaceRecog\MyPhoto\shanmukkha.jpg")
for gamma in np.arange(0.0, 3.5, 0.5):
    if gamma == 1:
        continue
    gamma = gamma if gamma > 0 else 0.1
    adjusted = adjust_gamma(original, gamma=gamma)
    cv2.putText(adjusted, "g={}".format(gamma), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Images", np.hstack([original, adjusted]))
    hist, bins = np.histogram(adjusted, 256, [0, 255])
    plt.fill(hist)
    plt.xlabel('pixel value')
    plt.show()
    cv2.waitKey(0)

