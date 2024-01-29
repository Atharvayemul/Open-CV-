import cv2 as cv


capture = cv.VideoCapture('Videos/dog.mp4')


def rescale(frame,scale = 0.75):
    # This method works for img videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


while True:
    isTrue,frame = capture.read()
    
    resize_vid = rescale(frame)
    
    cv.imshow('og',resize_vid)
    
    cv.imshow('Cap',frame)
    
    if(cv.waitKey(20) & 0xFF == ord('d')):
        break
    
    
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)


def changeres(width,height):
    # Only works for live video
    
    capture.set(3,width)
    capture.set(4,height)