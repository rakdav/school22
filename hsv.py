import cv2 as cv

img = cv.imread("butterfly.jpg")
width = 480
f = float(width) / img.shape[1]
new_size = (width, int(img.shape[0] * f))
res = cv.resize(img, new_size, interpolation=cv.INTER_AREA)
cv.imshow("resize", res)
hsv_img = cv.cvtColor(res, cv.COLOR_BGR2HSV)
color_low = (25, 60, 160)
color_high = (60, 255, 255)
only_object = cv.inRange(hsv_img, color_low, color_high)
moments = cv.moments(only_object, 1)
x_moment = moments['m01']
y_moment = moments['m10']
area = moments['m00']
x = int(x_moment / area)
y = int(y_moment / area)
cv.putText(only_object, "green", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.putText(only_object, "%d, %d" % (x, y), (x, y+50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.imshow("color_hsv", only_object)
cv.waitKey(0)
cv.destroyAllWindows()
