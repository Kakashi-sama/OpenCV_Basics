# Printing trackbar number on the image
import cv2
def nothing(x):
    print(x)
# Create a black image, a window

cv2.namedWindow('image')

# Create trackbars
cv2.createTrackbar('pos', 'image', 10, 400, nothing)

cv2.createTrackbar('Switch', 'image', 0, 1, nothing)

while 1:
    img = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\lena.jpg")

    pos = cv2.getTrackbarPos('pos', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos),(50, 150), font, 4, (0,0,255), 20)

    k = cv2.waitKey(1) &0XFF
    if k == 27:
        break

    s = cv2.getTrackbarPos('Switch', 'image')

    if s ==0 :
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image', img)

cv2.destroyAllWindows()