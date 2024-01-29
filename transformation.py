import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cat',img)

# Translating an image

def translate(img,x,y):
    transmatrix = np.float32([[1,0,x],[0,1,y]]) 
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmatrix,dimensions)

translated = translate(img,200,200)

# cv.imshow('Translated',translated)

# Rotation

def rotate(img,angle,rotpoint=None):
    (height,width) = img.shape[:2]
    
    if rotpoint is None:
        rotpoint = (width//2,height//2)
        
    rotMatrix = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img,rotMatrix,dimensions)

rotated = rotate(img,-45)
cv.imshow('Rotated',rotated)

# Resizing

resizd = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resize',resizd)

# Flipping

flip = cv.flip(img,1)

cv.imshow('Flipping',flip)

# Cropping

cropped = img[200:400,300:400]

cv.imshow('Cropped',cropped)
    

cv.waitKey(0)


    
    