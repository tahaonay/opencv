import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("contour.jpg",0)
plt.figure(),plt.imshow(img, cmap="gray"),plt.axis("off")


contours, hierarch =cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

external_c = np.zeros(img.shape)
internal_c = np.zeros(img.shape)

for i in range(len(contours)):
    #external_c
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_c,contours,i,255,-1)
    #internal_c
    else:
        cv2.drawContours(internal_c,contours,i,255,-1)
        
plt.figure(),plt.imshow(external_c, cmap="gray"),plt.axis("off")
plt.figure(),plt.imshow(internal_c, cmap="gray"),plt.axis("off")
