import cv2 as cv

# Reading images in opencv
path = r"D:\Data Science - AI - ML\Open_cv1\photos\black_cat.jpg"

img = cv.imread("photos\jagannath.jpg")

img2= cv.imread(path)

cv.imshow('cat',img) 

# Reading Videos

vid = cv.VideoCapture(r'videos\video1.mp4')

while True:
    isTrue, frame = vid.read()
    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break 

vid.release()
cv.destroyAllWindows()

cv.waitKey(0) 