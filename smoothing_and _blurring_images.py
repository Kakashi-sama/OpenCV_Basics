import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('resources\\Halftone_Gaussian_Blur.jpg')
# img = cv2.imread('resources\\water.png')

img = cv2.imread('resources\\lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25

TwoDConv = cv2.filter2D(img, -1, kernel)  # Homogenous Filter, Two Dimensional Convolution

AverageBlur = cv2.blur(img, (5, 5))  # Averaging Algorithm for blurring the image

G_blur = cv2.GaussianBlur(img, (5, 5), 0)  # Gaussian Filter Algorithm

MedianFilter = cv2.medianBlur(img, 3)  # Median Filter

BilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)  # Bilateral Filter

titles = ['images', '2DConvolution', 'AverageBlur', 'GaussianBlur', 'MedianBLur', 'BilateralFilter']
images = [img, TwoDConv, AverageBlur, G_blur, MedianFilter, BilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
