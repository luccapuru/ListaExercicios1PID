import numpy
import cv2

img = numpy.ones((300,300,1),numpy.uint8)*255
cv2.imshow('image',img)
# img[0, 0, 0] = 0
# cv2.imshow('image2',img)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if j <= 255:
            img[i, j, 0] = j
        else:
            img[i, j, 0] = 255

cv2.imshow('image2',img)
cv2.waitKey()