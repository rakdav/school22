import cv2 as cv

image = cv.imread("butterfly.jpg")
# cv.imshow("image1", image)
width = 480
f = float(width) / image.shape[1]
new_size = (width, int(image.shape[0] * f))
res = cv.resize(image, new_size, interpolation=cv.INTER_AREA)
# cv.imshow("resize", res)
crop = res[20:200, 20:270]
(h, w) = crop.shape[:2]
center = (w / 2, h / 2)
prepObj = cv.getRotationMatrix2D(center, 180, 1.0)
rotated = cv.warpAffine(crop, prepObj, (w, h))
cv.imshow("crop", crop)
# cv.imshow("rotated", rotated)
flipped = cv.flip(crop, 1)
cv.imshow("flipped", flipped)
cv.imwrite("flip.png", flipped)
cv.waitKey(0)
