import cv2
import time

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
