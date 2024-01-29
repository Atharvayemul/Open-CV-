import cv2 as cv


img = cv.imread('Photos/cat.jpg')


cv.imshow('Cat',img)

cv.waitKey(0)

# Wait key 0 means wait infinity for any key presssed

# This means if any key is pressed the window is closed