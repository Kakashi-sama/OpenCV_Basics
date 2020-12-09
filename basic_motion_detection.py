import cv2

cap = cv2.VideoCapture('resources\\')

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("inter", frame)

    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()
