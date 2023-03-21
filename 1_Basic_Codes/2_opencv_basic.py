import cv2
import time

img = cv2.imread("roi.jpg",0)  # 0= grayscale

# for Image
cv2.imshow("Ilk resim", img)
k = cv2.waitKey(0) &0xFF

if k==27:  # esc
    cv2.destroyAllWindows()
elif k== ord('s'): # s
    cv2.imwrite("messi_gray.png",img)
    cv2.destroyAllWindows()
    

# ------------------------------
# for Video
video_name ="MOT17-04-DPM.mp4"
cap = cv2.VideoCapture(video_name)

print("Genişlik: ",cap.get(3))
print("Yükseklik: ",cap.get(4))

if cap.isOpened() == False:
    print("Hata video açılmadı")

while True:
    ret, frame = cap.read()
    
    if ret== True:
        time.sleep(0.01) # kullanmazsak çok hızlı akar
        cv2.imshow("Video",frame)

    else: 
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release() # stop capture
cv2.destroyAllWindows() 
