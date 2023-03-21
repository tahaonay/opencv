import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8) # siyah resim

print(img.shape)


cv2.imshow("siyah",img)


# line
#       (resim, başlangıç, bitiş, renk(BGR),kalınlık)
cv2.line(img,   (50,50), (200,200), (0,255,0), 3) 
cv2.imshow("Cizgi",img)

# rectangle
cv2.rectangle(img, (100,100),(300,300),(0,0,255),2)
cv2.imshow("Kare",img)

# rectangle fill
cv2.rectangle(img, (200,200),(300,300),(0,0,255),cv2.FILLED)
cv2.imshow("Kare",img)

# circle 
# (resim başlangıç,yarıçap,)
cv2.circle(img, (300,300),50,(255,0,0))
cv2.imshow("Cember",img)

# circle fill
cv2.circle(img, (300,300),50,(255,0,0),cv2.FILLED)
cv2.imshow("Cember",img)

# TEXT
# (resim, başlangıç,font,kalınlık,renk)
cv2.putText(img,"Resim",(350,350), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Yazi",img)


