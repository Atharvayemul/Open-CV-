import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# Bitwise And --intesection
# Basically returns the intersection between the two images


bitwise_and = cv.bitwise_and(rectangle,circle)

cv.imshow('Bitwiseand',bitwise_and)

# Bitwise or --> Non-intersecting and intersecting 

birwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwiseor',birwise_or)

# Bitwise XOR --> Non-intersecting

bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('BitwiseXor',bitwise_xor)

# Bitwise Not

bitwise_not = cv.bitwise_not(circle)
cv.imshow('Rectangle_not',bitwise_not)



cv.waitKey(0)