import cv2 as cv

img= cv.imread(r'photos\jagannath.jpg')

# changing the dimension of frame 
def rescaleFrame(frame, scale =0.75):
    #works for images, videos, live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions,interpolation= cv.INTER_AREA)

def changeRes(width, height) :
    # only works for live videos
    vid.set(3, width)
    vid.set(4, height)

cv.imshow("Lord", rescaleFrame(img, .3))

cv.waitKey(0)
# Reading Videos

vid = cv.VideoCapture(r'videos\video1.mp4')

while True:
    isTrue, frame = vid.read()

    frame_resize = rescaleFrame(frame)

    cv.imshow("video", frame)
    cv.imshow("video resized", frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break 

vid.release()
cv.destroyAllWindows()