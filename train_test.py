import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
print("Imports Complete")
img =cv.imread("test-img\test.jpg")
cv.imshow("Output", img)
cv.waitKey(0)
cv.destroyAllWindows()
