import cv2
import numpy as np

img = cv2.imread('resources\\road.png')
temp = np.copy(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# cv2.imshow('canny', edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
Plines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off values of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off values of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * a)
    # x2 stores the rounded off values of (r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off values of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

for line in Plines:
    x1, y1, x2, y2 = line[0]
    cv2.line(temp, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('HoughLineP', temp)
# cv2.imshow('HoughLine', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
