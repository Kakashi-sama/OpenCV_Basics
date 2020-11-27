import cv2
import numpy as np

img = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\Vamshi photo.jpg", 1)

img = np.zeros([512, 512, 3])

img = cv2.line(img, (0,0), (255,255), (0,0,255), 5)

img = cv2.arrowedLine(img, (0,280), (255,280), (0,0,255), 5)

img = cv2.rectangle(img, (0,0), (300,300), (0,0,255), 20)

img = cv2.circle(img, (150,150), 100, (0,255,0), 5)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

img = cv2.putText(img, 'Vamshi', (120,440), font, 1, (255,0,255), 1, cv2.LINE_AA)

cv2.imshow('frame', img)

cv2.waitKey(0) & 0xFF

cv2.destroyAllWindows()