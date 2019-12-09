import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('darah4.jpg')

kernel = np.ones((8,8),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.show()