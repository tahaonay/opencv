import cv2
import matplotlib.pyplot as plt


chos = cv2.imread("chocolates.jpg",0)
cho = cv2.imread("nestle.jpg",0)

plt.figure(),plt.imshow(chos, cmap="gray"),plt.axis("off")
plt.figure(),plt.imshow(cho, cmap="gray"),plt.axis("off")


# %% orb  köşe-kenar özellikleri gibi
orb = cv2.ORB_create()

# anahtar nokta tespiti
kp1, des1 = orb.detectAndCompute(cho, None)  # maskeleme yok => None
kp2, des2 = orb.detectAndCompute(chos, None)


#brute-force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

#noktaları eşleştir
matches = bf.match(des1,des2)

#mesafeye göre sıralama
matches = sorted(matches, key=lambda x:x.distance)

# eşleşenleri görselleştir ilk 20 tanesi
plt.figure()
img_match = cv2.drawMatches(cho,kp1,chos,kp2,matches[:20],None, flags =2)
plt.imshow(img_match), plt.axis("off")


# %%sift
sift = cv2.xfeatures2d.SIFT_create()

#bf tanımlama
bf=cv2.BFMatcher()

#anahtar nokta tespit
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(chos, None)

matches = bf.knnMatch(des1, des2, k=2)  # 2 eşleşme

guzel_es =[]
for match1,match2 in matches:
    if match1.distance < 0.75*match2.distance:
        guzel_es.append([match1])
        
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho,kp1,chos,kp2,guzel_es,None, flags=2)
plt.imshow(sift_matches), plt.axis("off"),plt.title("sift")





