import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("unnamed.jpg")
cv.imshow("Display window", img)
k = cv.waitKey(0)
