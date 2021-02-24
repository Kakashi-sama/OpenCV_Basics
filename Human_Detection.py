from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Loop over the image paths
for imagePath in paths.list_images('persons'):
    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=min((400, image.shape[1])))
    orig = image.copy()

    # Detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('without NMS', orig)
    cv2.waitKey(0)
