"""""
import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

a = 1

while True:
    a = a+1
    check,frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Dhodis',gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


print(a)
video.release()
cv2.destroyAllWindows()


import cv2

video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('dhodis', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

"""""

import cv2
from datetime import datetime

video = cv2.VideoCapture(0)
# print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(video.get(cv2.CAP_PROP_FRAME_WIDTH))

video.set(3, 700000)
video.set(4, 700000)

# print(video.get(3))
# print(video.get(4))

while video.isOpened():
    check,frame = video.read()
    if check:
        frame = cv2.flip(frame, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(int(video.get(3))) + '    Height: '+ str(int(video.get(4)))
        datet = datetime.now()
        dateo = date_time = datet.strftime("%d/%m/%Y, %H:%M:%S")
        frame = cv2.putText(frame, dateo, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('dhodi', frame)

        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
