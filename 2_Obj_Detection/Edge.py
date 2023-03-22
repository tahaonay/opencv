import cv2
import matplotlib.pyplot as plt
import numpy as np


# Resim içe aktar
img = cv2.imread("london.jpg",0)
plt.figure()

plt.imshow(img,cmap="gray"),plt.axis("off")

# kenarları çizdirme
#edges = cv2.Canny(image=img, threshold1 =0, threshold2=255)
edges = cv2.Canny(img,0,255)
plt.figure(), plt.imshow(edges,cmap="gray"),plt.axis("off")



# %% median değerlere göre kenar alma
med_val = np.median(img)
print(med_val)

low = int(max(0, (1-0.33)*med_val))
high = int(min(255, (1+0.33)*med_val))

edges = cv2.Canny(img,low,high)
plt.figure(), plt.imshow(edges,cmap="gray"),plt.axis("off")

# %% blur uygulayarak edge tespiti
# ksize artarsa detay azalır, kenar daha belirginleşir
blured_img = cv2.blur(img,ksize=(5,5))
plt.figure(), plt.imshow(blured_img,cmap="gray"),plt.axis("off")

med_val = np.median(blured_img)
print(med_val)

low = int(max(0, (1-0.33)*med_val))
high = int(min(255, (1+0.33)*med_val))

edgesBlur = cv2.Canny(blured_img,low,high)
plt.figure(), plt.imshow(edgesBlur,cmap="gray"),plt.axis("off")
