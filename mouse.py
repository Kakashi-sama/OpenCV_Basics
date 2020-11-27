import cv2
import numpy as np

#for i in dir(cv2):
 #   if 'EVENT' in i:
  #      print(i)

# THE ABOVE CODE can be simplified as:(pretty cool)
#print([i for i in dir(cv2) if 'EVENT' in i])

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x,y), font, .5, (255,255,255), 2,)
        cv2.imshow('dhodi', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 2]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(blue) + ', '+ str(green) + ', ' + str(red)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2, )
        cv2.imshow('dhodi', img)

#img = np.zeros((512,512,3))
#img = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\Vamshi photo.jpg", 1)
img = cv2.imread("C:\\Users\\bojan\\PycharmProjects\\pyTest\\resources\\messi5.jpg", 1)
cv2.imshow('dhodi', img)
cv2.setMouseCallback('dhodi', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()