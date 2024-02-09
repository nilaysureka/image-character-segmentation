import cv2
img=cv2.imread(r'C:\Users\nilay\Downloads\DTU_UAS Sofware Round-2\Test_images\1.jpeg')
imrGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Img",imgGray)
imgCanny =cv2.Canny(img,100,100)
cv2.imshow("Canny Image",imgCanny)
#ker=np.ones((5,5),np.uint8)

import numpy as np
ker=np.ones((5,5),np.uint8)
imgDial=cv2.dilate(imgCanny,ker,iterations=1)
cv2.imshow("Dial Image",imgDial)

import pytesseract

img=cv.imread(r"C:\Users\nilay\Downloads\DTU_UAS Sofware Round-2\Test_images\1.jpeg")
imgGray=cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("OUTPUT",img)

'''def segment_characters(image_path):
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)  # Adjust kernel size as needed
    thresh = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
'''
def segment_characters(image_path):
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)  # Adjust kernel size as needed
    thresh = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    min_area = 50
    segmented_characters = []
    for cntr in contours:
        x, y, w, h = cv.boundingRect(cntr)
        aspect_ratio = float(w) / h
        area = cv.contourArea(cntr)
        if aspect_ratio > 0.2 and aspect_ratio < 1.5 and area > min_area:
            char_image = image[y:y+h, x:x+w]
            segmented_characters.append(char_image)
    return segmented_characters

image_path = r"C:\Users\nilay\Downloads\DTU_UAS Sofware Round-2\Test_images\1.jpeg"
characters = segment_characters(image_path)
for i, char_image in enumerate(characters):
    cv.imshow(f"Character {i+1}", char_image)
  
cv2.waitKey(0)
