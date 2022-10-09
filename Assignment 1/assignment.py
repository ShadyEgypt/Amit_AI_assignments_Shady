import cv2
import numpy as np

img = cv2.imread('scan.jpg')
w = 400
h = int(w*1.414)
pointsA = np.float32([[320,15], [700,215], [85,610], [530, 780]])
pointsB = np.float32([[0,0], [w,0], [0,h], [w, h]])



# the perspective to grab the screen
M = cv2.getPerspectiveTransform(pointsA, pointsB)
warp = cv2.warpPerspective(img, M, (w, h))

cv2.imshow("warp", warp)

ret,thresh1 = cv2.threshold(warp, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary', thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()