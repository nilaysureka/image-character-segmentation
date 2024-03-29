import cv2
import numpy as np
#Packages Imported
img=cv2.imread(r'Resources\1.jpeg')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Setting Colour tone to grey
cv2.imshow("Gray Img",imgGray)
imgCanny =cv2.Canny(img,100,100)
cv2.imshow("Canny Image",imgCanny) #canny edges detection
'''ker=np.ones((5,5),np.uint8)
imgDial=cv2.dilate(imgCanny,ker,iterations=1) '''
imgBlur=cv2.GuasianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image",imgBlur)

path='Resources/1.jpg'
def getContours(img):
  contours,hierarchy= cv2.findContours(img,cv2.RETR_EXTERNAL)
