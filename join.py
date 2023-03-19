import cv2
import numpy as np

# resmi içeri aktarma
img = cv2.imread("lenna.png")
# resmi gösterme
cv2.imshow("Resim",img)


# yatay birleştirme
hor = np.hstack((img,img))
cv2.imshow("Yatay",hor)
# dikey birleştirme
ver = np.vstack((img,img))
cv2.imshow("Dikey",ver)

