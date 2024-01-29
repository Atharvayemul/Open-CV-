import cv2 as cv

import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

# cv.imshow('Blank',blank)


# Paint the image a certain color

# blank[200:300,300:400] = 0,0,255

# cv.imshow('Green',blank)

# 2.draw a rectangle

rectangle = cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)

# cv.imshow('rec',rectangle)

# draw a circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,(0,0,225),thickness=-1)

# cv.imshow('Circle',blank)


# 4. draw a line

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)

# cv.imshow('Line',blank)

# 5 write a text on image

cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)

cv.imshow('text',blank)


cv.waitKey(0)
