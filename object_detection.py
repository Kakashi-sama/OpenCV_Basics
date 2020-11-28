import cv2
import numpy as np

l_b = np.array([110, 50, 50])
u_b = np.array([130, 255, 255])

while True:
    frame = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\smarties.png")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, l_b, u_b)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
