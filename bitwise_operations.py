import cv2
import numpy as np

img1 = np.zeros((250,499,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\bit_image.png")

#bitAnd = cv2.bitwise_and(img1, img2)
#bitOr = cv2.bitwise_or(img1, img2)
#bitXOr = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
#cv2.imshow("bitand", bitAnd)
#cv2.imshow("bitor", bitOr)
#cv2.imshow("bitxor", bitXOr)
cv2.imshow("bitnot1", bitNot1)
cv2.imshow("bitnot2", bitNot2)


cv2.waitKey(0)
cv2.destroyAllWindows()