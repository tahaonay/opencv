import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

"""
OPENCV_OBJECT_TRACKERS = {"csrt"      : cv2.TrackerCSRT_create,
                          "kcf"       : cv2.TrackerKCF_create,
                          "boosting"  : cv2.TrackerBoosting_create,
                          "mil"       : cv2.TrackerMIL_create,
                          "tld"       : cv2.TrackerTLD_create,
                          "medianflow": cv2.TrackerMedianFlow_create,
                          "mosse"     : cv2.TrackerMOSSE_create}

tracker_name = "kcf"
tracker = OPENCV_OBJECT_TRACKERS[tracker_name]()
"""
print("Tracker:" ,cv2.TrackerKCF_create)
tracker = cv2.TrackerKCF_create()
gt = pd.read_csv("gt_new.txt")

video_path = "MOT17-13-SDP.mp4"
cap = cv2.VideoCapture(video_path)

#parameters
initBB = None
fps = 25
frame_Number = []
f = 0
success_track_frame_success = 0
track_list = []
start_time = time.time()   # time is starting here

while True:
    time.sleep(1/fps)
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, dsize=(960,540))
        (H,W) = frame.shape[:2]
        #gt
        car_gt = gt[gt.frame_no ==f]
        if len(car_gt != 0):
            x = car_gt.x.values[0]
            y = car_gt.y.values[0]
            w = car_gt.w.values[0]
            h = car_gt.h.values[0]

            center_x = car_gt.center_x.values[0]
            center_y = car_gt.center_y.values[0]

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame,(center_x,center_y),2,(0,0,255),-1)

        #box
        if initBB is not None:
            (success, box) = tracker.update(frame)

            if f<=np.max(gt.frame_no):
                (x,y,w,h) = [int(i) for i in box]
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                success_track_frame_success +=1
                track_center_x = int(x+w/2)
                track_center_y = int(y+h/2)
                track_list.append([f,track_center_x,track_center_y])

            info = [("Tracker",tracker),
                    ("Success","Yes" if success else "No")]
            for (i,(o,p)) in enumerate(info):
                text = "{}: {}".format(o,p)
                cv2.putText(frame, text, (10,H-(i*20)-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
        
        #Image
        cv2.putText(frame, "Frame number: "+ str(f), (10,30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
        cv2.imshow("frame",frame)

        # key
        key = cv2.waitKey(1) & 0xFF

        if key == ord("t"):
            initBB = cv2.selectROI("Frame",frame,fromCenter= False)
            tracker.init(frame, initBB)
        
        elif key == ord("q"):
            break

        #frame
        frame_Number.append(f)
        f +=1

    else:
        break


cap.release()
cv2.destroyAllWindows()

