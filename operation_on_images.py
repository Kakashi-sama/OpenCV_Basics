import cv2
import numpy as np

img = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\messi5.jpg", 1)
img2 = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\opencv-logo.png",1)

print(img.shape) # returns tuple of number of rows, columns, and channels
print(img.size) # returns total number of pixels accessed
print(img.dtype)# returns image datatype obtained
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0) #Similar to add but can add weights to the images
cv2.imshow('frame', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

