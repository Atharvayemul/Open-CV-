import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)


# Converting to a grayScale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)


# Blur

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

cv.imshow('Blur', blur)

# Edge Cascade

canny = cv.Canny(img, 125, 175)

cv.imshow('Canny edges', canny)

# Dialating the image

dilated = cv.dilate(canny, (3, 3), iterations=1)

cv.imshow('Dialated', dilated)


# Eroding
eroding = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroding)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# The inter_Area interpolation is used when the size of original image is large than resize one
cv.imshow('resize', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
