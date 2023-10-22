import cv2 as cv

capImg = cv.VideoCapture("sveto.mp4")
while capImg.isOpened():
    ret, frame = capImg.read()
    if frame is None:
        break
    cv.imshow("video", frame)
    key_press = cv.waitKey(30)
    if key_press == ord('q'):
        break
capImg.release()
cv.destroyAllWindows()
