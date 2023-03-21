import cv2
import numpy as np

# import image
img = cv2.imread("lenna.png")
# show image
cv2.imshow("Resim",img)


# horizontal join
hor = np.hstack((img,img))
cv2.imshow("Yatay",hor)
# vertical join
ver = np.vstack((img,img))
cv2.imshow("Dikey",ver)

