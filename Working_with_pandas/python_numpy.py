import numpy
import cv2

n=numpy.arange(27)
print(n)
n=n.reshape(3,3,3)
print(n)
print(n[2][0][0])
print("------------------------------------------------------")

img_ = cv2.imread("smallgray.png",0)
print(img_)

cv2.imwrite("newsmallgray.png",img_)