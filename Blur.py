import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")



# bluring (detayı azaltır, gürültüyü engeller)
img =cv2.imread("NYC.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

"""
ortalama bulanıklaştırma
"""
dst2 = cv2.blur(img, ksize=(3,3))
plt.figure()
plt.imshow(dst2),plt.axis("off"),plt.title("ortalama"),plt.show()


"""
Gaussian blur
"""
gb = cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gb),plt.axis("off"),plt.title("GaussBlur"),plt.show()

"""
Medyan Blur
"""
mb = cv2.medianBlur(img,ksize=3)
plt.figure()
plt.imshow(mb),plt.axis("off"),plt.title("MedianBlur"),plt.show()

# %% Noise
def gaussianNoise(image):
    row,col,ch=image.shape
    mean =0
    var =0.05
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss

    return noisy

img = cv2.imread("NYC.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255

plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

gaussianNoiseImage = gaussianNoise(img)

plt.figure()
plt.imshow(gaussianNoiseImage),plt.axis("off"),plt.title("gaussNoise"),plt.show()

#gaussian blur
gb2 = cv2.GaussianBlur(gaussianNoiseImage,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gb2),plt.axis("off"),plt.title("with GaussBlur"),plt.show()

# %% tuz biber

def saltPepperNoise(image):
    row,col,ch=image.shape
    s_vs_p = 0.5
    amount= 0.004
    noisy = np.copy(image)
    
    #salt
    num_salt = np.ceil(amount*image.size*s_vs_p)
    coords= [np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    #pepper
    num_pepper = np.ceil(amount*image.size*(1-s_vs_p))
    coords= [np.random.randint(0,i-1,int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)

plt.figure()
plt.imshow(spImage),plt.axis("off"),plt.title("SP Image"),plt.show()

mb2 = cv2.medianBlur(spImage.astype(np.float32),ksize=3)
plt.figure()
plt.imshow(mb2),plt.axis("off"),plt.title("with MedianBlur"),plt.show()



