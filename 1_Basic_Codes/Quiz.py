import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("odev1.jpg",0)   #0=gri

#resmi çizdirme
plt.figure()
plt.imshow(img, cmap ="gray")

#boyut
print("boyut= ",img.shape)

#4/5 oranı yeniden boyulandırma
img2 = cv2.resize(img,(688,455))
plt.figure()
plt.imshow(img2, cmap ="gray")

# yazı ekleme
img3= cv2.putText(img, "kopek",(350,100) ,cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0))
plt.figure()
plt.imshow(img3, cmap ="gray")

# threshold
ret,thresh1 = cv2.threshold(img, 50,255,cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh1, cmap="gray")

#gaussian bulanıklaştırma
img_blured = cv2.GaussianBlur(img,(5,5),0) 
plt.figure()
plt.imshow(img_blured, cmap="gray")

# laplacian
img_lap = cv2.Laplacian(img,ddepth=cv2.CV_64F)
plt.figure()
plt.imshow(img_lap, cmap="gray")
plt.show()

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(img_hist)
