import cv2
from PIL import Image
cv2.namedWindow('panda', cv2.WINDOW_NORMAL)
img = cv2.imread("E:/1.jpg", 1)
img = cv2.resize(img, (300, 300))
cv2.imshow("panda", img)
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("E:/2.jpg", img)