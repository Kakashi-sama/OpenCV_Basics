import cv2

# Creating a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("resources\\haarcascade_frontalface_default.xml")

# reading the Image
img = cv2.imread("resources\\Vamshi photo.jpg", 1)

# Reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
