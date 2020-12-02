"""""
import cv2  # Gaussian and Laplacian Pyramids
import numpy as np

img = cv2.imread('resources\\lena.jpg')

lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)

cv2.imshow('Original image', img)
cv2.imshow('pyrDown1', lr1)
cv2.imshow('pyrDown2', lr2)
cv2.imshow('pyrUp1', hr2)  # hr1 and lr1 are not the same

cv2.waitKey(0)
cv2.destroyAllWindows()
"""""
# Gaussian Pyramid has 2 functions PyrUp and PyrDown.
# Laplacian Pyramid has no method defined explicitly.

import cv2

img = cv2.imread('resources\\lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level gaussian pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)


cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
