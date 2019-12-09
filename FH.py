import cv2;
import numpy as np;
 
# Read image
im_in = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE);
 
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(im_in,kernel,iterations = 1)
##erosion = cv2.erode(dilation,kernel,iterations = 1)

th, im_th = cv2.threshold(dilation, 220, 255, cv2.THRESH_BINARY_INV);

cv2.imshow("Thresholded Image", im_th)


cv2.waitKey(0)