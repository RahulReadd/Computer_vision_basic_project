import cv2 as cv
from cv2 import FONT_HERSHEY_TRIPLEX
import numpy as np

blank = np.zeros((500,500,3),dtype= 'uint8')
cv.imshow('blank', blank)


# # 1. paint the image a certain colour
# blank[:] = 0, 255, 0
# cv.imshow('Green',blank)

# blank[200:400, 300: 400] = 0,0,255
# cv.imshow('red',blank)

cv.rectangle(blank,(100,200),(250,250),(0,255,0), thickness= -1)

cv.imshow('rectangle', blank)

# Drawing a circle 
cv.circle(blank,(250,250),50,(0,100,200),thickness=5)
cv.circle(blank,(100,200),50,(0,100,200),thickness=5)

cv.imshow('circle', blank)

# Drawing a line
cv.line(blank,(100,200),(250,250),(200,50,100),thickness=5)

cv.imshow('Line', blank)

# write text 
cv.putText(blank, "Namaste! it's open cv", (0,450),cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255),thickness= 2)

cv.imshow ('texted', blank )

cv.waitKey(0)