import cv2

img = cv2.imread("lenna.png")

print("resim Boyutu : ",img.shape)
cv2.imshow("orijinal",img)


#resized
img_resized = cv2.resize(img,(800,800))
cv2.imshow("resized",img_resized)

#crop
img_cropped = img[:250,0:250]
cv2.imshow("cropped",img_cropped)

img_cropped2 = img[200:500,100:450]
cv2.imshow("cropped2",img_cropped2)
