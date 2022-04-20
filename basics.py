import cv2 as cv

img = cv.imread(r'photos\audio_mixer.jpg')
cv.imshow('Audio_mixture',img)

# Convert to Grayscale 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Audio_mix_gray', gray)

# Blur
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade

canny = cv.Canny(img, 123,150)
cv.imshow('Canny edges', canny)

# Dialating the image
dilated= cv.dilate(canny,(7,7), iterations= 3)
cv.imshow('Dialated', dilated)

eroded= cv.erode(dilated, (7,7),iterations=3)
cv.imshow('Eroded',eroded)

# Resize
resized = cv.resize(img, (500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

# Cropping
cropped = img[50 : 200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
