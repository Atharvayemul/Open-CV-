import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats',img)

# Averaging

average = cv.blur(img,(3,3))
cv.imshow('Average blur',average)

# Gaussian blur

gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gauss)

# Median blur

median_blur = cv.medianBlur(img,3)
cv.imshow('Median Blur',median_blur)

# Bilateranl blur

bilateral_blur = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral_blur)


cv.waitKey(0)