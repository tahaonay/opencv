#OpenCV ile görüntü işleme

# %% Resmi içeri aktarma
import cv2
img = cv2.imread("roi.jpg",0) # 0= grayscale

#görselleştir
cv2.imshow("Ilk resim", img)
k = cv2.waitKey(0) &0xFF

if k==27:  # esc
    cv2.destroyAllWindows()
elif k== ord('s'): # s
    cv2.imwrite("messi_gray.png",img)
    cv2.destroyAllWindows()
    
