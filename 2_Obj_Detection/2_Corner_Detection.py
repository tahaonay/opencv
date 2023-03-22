import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.jpg",0)
img = np.float32(img) # float tipine dönüştürdük

plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.show()
print(img.shape)

# %%harris corner detection
dst = cv2.cornerHarris(img, blockSize=2, ksize=3, k=0.04)
plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off"),plt.show()

# belirgin hale getirme genişletme ile
dst = cv2.dilate(dst, None)
img[dst> 0.2*dst.max()] = 1
plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off"),plt.show()


# %% shi tamsai detection

corners = cv2.goodFeaturesToTrack(img,100,0.01,10) #(resim, köşe sayısı, kalite, köşe arası mesafe)
corners = np.int64(corners)
for i in corners:
    x,y = i.ravel() # düzleştirme
    cv2.circle(img, (x,y),3,(125,125,125),cv2.FILLED)
    
plt.imshow(img)
plt.axis("off")
     

