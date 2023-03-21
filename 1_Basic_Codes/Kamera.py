import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

# video kaydet
writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))  #(isim, windowsa özel kod,fps,çerçeve)

while True:
    ret, frame = cap.read()            
    cv2.imshow("Video",frame)           
    
    #save
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
    
cap.release()
writer.release()
cv2.destroyAllWindows()

