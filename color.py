import cv2 as cv

img = cv.imread("butterfly.jpg")
width = 480
f = float(width) / img.shape[1]
new_size = (width, int(img.shape[0] * f))
res = cv.resize(img, new_size, interpolation=cv.INTER_AREA)
cv.imshow("resize", res)
low_color = (0, 0, 100)
high_color = (100, 100, 255)
only_object = cv.inRange(res, low_color, high_color)
cv.imshow("only object", only_object)
cv.waitKey(0)
cv.destroyAllWindows()