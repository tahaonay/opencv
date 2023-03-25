import cv2
import os

files = os.chdir("9-CatFacesDetection")
files = os.listdir()

img_path_list =[]

for i in files:
    if i.endswith("jpg"):
        img_path_list.append(i)

print(img_path_list)

for j in img_path_list:
    img = cv2.imread(j)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    rects = detector.detectMultiScale(gray,scaleFactor= 1.045,minNeighbors=2)
    for (i,(x,y,w,h)) in enumerate(rects):
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),3)
            cv2.putText(img,"Kedi: {}".format(i+1),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.55,(0,255,255),2)

    cv2.imshow(j,img)

    if cv2.waitKey(0) & 0xFF == ord("q"): continue

    
