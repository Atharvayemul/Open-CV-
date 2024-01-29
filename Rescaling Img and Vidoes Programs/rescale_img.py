import cv2 as cv


img = cv.imread('Photos/cat.jpg')

cv.imshow('Original',img)


def rescale(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


resize_img = rescale(img)

cv.imshow('Change',resize_img)

cv.waitKey(0)