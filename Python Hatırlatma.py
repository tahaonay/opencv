# %% spyder giriş
print("İLK spyder")
for i in range(10):
    print("i= ",i)
    
# %% değişkenler
tamsayi =10
ondalikli = 3.4
print(tamsayi)
print(ondalikli)

# 4 işelem
pi= 3.14
katsayi =2
carpım = 3*pi*katsayi
print(carpım)

# print
print("carpım= {}".format(carpım))
print("carpım= %.1f"%carpım)

veriyolu= "veri" + "\\" + "img" + ".png"
print(veriyolu)
# %% liste
liste= [1,2,3,4,5,6]
print(liste)
meyve= ["elma","muz","armut","kivi"]
print(meyve[2])

liste.append(8)
print(liste)
liste.remove(2)
print(liste)
liste.sort()
print(liste)
# %% tuple  
# Değiştirilemez veri tipi
tuple_veri = (1,2,3,3,3,6,7)

print(tuple_veri)
print(tuple_veri[3:])
print(tuple_veri.count(3))

tuple_xyz = (1,2,3)
x,y,z = tuple_xyz
print(x,y,z)

# %% deque
from collections import deque

dq= deque(maxlen =3)

dq.append(1)
print(dq)
dq.append(2)
print(dq)
dq.append(3)
print(dq)
dq.append(4)  # yeni veri eklendi, ilk veri kaltı
print(dq)
dq.appendleft(4)
print(dq)

dq.clear()
print(dq)
# %% dictionary
sozluk = {"bir":1,
          "ankara":6,
          "istanbul":34}

print(sozluk["istanbul"])
# %% if else elif
sayi1 =5
sayi2 =10
if sayi1<sayi2:
    print("küçük")
else:
    print("büyük")
    
liste = [1,2,3,4,5]
deger = 10
if deger in liste:
    print("{} değeri liste içinde".format(deger))
else:
    print("{} değeri liste içinde değil".format(deger))
# %% döngüler
toplam =0
ktoplam =0
for i in range(10):
    print(i," = ",i**2)
    toplam += i
    ktoplam += i**2
print(toplam, " = ",ktoplam)



tuple1 = ((1,2,3),(4,5,6))

for x,y,z in tuple1:
    print(x,y,z)
    
# %% fonksiyonlar
def karealma(sayi):
    return sayi**2

print(karealma(5))

def dairecap(yaricap):
    yc= 3.14*yaricap*2
    print("darirenin çevresi = %.2f"%(yc))
    
dairecap(10)

# %% numpy
import numpy as np
 
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi.shape) # array boyutu

dizi2 = dizi.reshape(3,5)
print("şekli: ",dizi2.shape)
print("boyutu: ",dizi2.ndim)
print("büyüklüğü: ",dizi2.size)
print("veritipi:", dizi2.dtype.name)

# 2 boyutlu array
dizi2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,4]])
print(dizi2d)

# sıfırlardan oluşan array
sifir_dizi =np.zeros((3,4))
print(sifir_dizi)

# birlerden oluşan array
bir_dizi =np.ones((3,4))
print(bir_dizi)

dizi_aralik = np.arange(5,35,5)
print(dizi_aralik)

dizi_bosluk = np.linspace(5,35,5)
print(dizi_bosluk)

float_array = np.float32([[1,2],[3,4]])
print(float_array)

# array işlemler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

# dizi elemanları toplama
print(np.sum(a))
print("max: ",np.max(a))
print("min: ",np.min(a))
print("ort: ",np.mean(a))
print("medyan: ",np.median(a))

# rastgele sayı üretme
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

#index

dizi= np.array([1,2,3,4,5,6,7])
print(dizi[1])
print(dizi[0:4])   # ilk 4
print(dizi[::-1])   #ters çevir

dizi2d = np.array([[4,5,6,7],[7,8,9,0]])
print(dizi2d[0,0])
print(dizi2d[1,2])

# 1.sutün tüm satır
print(dizi2d[:,1])

# 1.satır tüm sutün
print(dizi2d[1,:])

print(dizi2d[1,1:4])

# vektor haline getirme
dizi2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2d)

vektor = dizi2d.ravel()
print(vektor)

maximum_sayi_index = vektor.argmax()
print(maximum_sayi_index)

# %% pandas
import pandas as pd

# sozlük oluştur
dictionary ={ "isim":["ali","veli","kenan","murat","ayse","hilal"],
              "yas":[15,16,17,33,45,66],
              "maas":[100,150,240,350,110,220]}

veri = pd.DataFrame(dictionary)
print(veri)

#ilk 5 satır
print(veri.head(5))
#sütunlar
print(veri.columns)
# veri bilgisi
print(veri.info())
#istatistiksel veriler
print(veri.describe())
# yaş sutünü
print(veri["yas"])
# sutün ekleme
veri["sehir"] = ["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]
# yas sütunu
print(veri.loc[:,"yas"])
# yas sütunu ilk 3 satır
print(veri.loc[:2,"yas"])
# yas ve sehir arası, ilk 3 satır
print(veri.loc[:2,"yas":"sehir"])
# isim ve sehir, ilk 3 satır
print(veri.loc[:2,["isim","sehir"]])
# satırları tersten yazdır
print(veri.loc[::-1,:])
# yas sutünü iloc ile yazdır
print(veri.iloc[:,1])
# yas ve isim ilk 3 satır
print(veri.iloc[:2,[0,1]])



# filtreleme
dictionary ={ "isim":["ali","veli","kenan","murat","ayse","hilal"],
              "yas":[15,16,17,33,45,66],
              "sehir":["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"]}

veri = pd.DataFrame(dictionary)
print(veri)

# Ankarada yaşayan insanları yaş ortalaması

#22 yaşından büyükler
filtre1= veri.yas > 22
filtreli_veri= veri[filtre1]
print(filtreli_veri)

# ortalama yas
ortalama_yas = veri.yas.mean()

veri["YAS_GRUBU"] =["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)




# birleştirme
sozluk1= { "isim":["ali","veli","kenan"],
           "yas":[15,16,17],
           "sehir":["İzmir","Ankara","Konya"]}
veri1= pd.DataFrame(sozluk1)


sozluk2= { "isim":["murat","ayse","hilal"],
           "yas":[33,45,66],
           "sehir":["Ankara","Ankara","Antalya"]}
veri2= pd.DataFrame(sozluk2)

# dikey
veri_dikey = pd.concat([veri1,veri2],axis=0)
# yatay
veri_yatay = pd.concat([veri1,veri2],axis=1)


# %% Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.array ([1,2,3,4])
y = np.array ([4,3,2,1])

plt.figure()
plt.plot(x,y, color="red",alpha= 0.7,label = "line")
plt.scatter(x, y,color ="blue", alpha=0.4, label="scatter")   # noktalar
plt.title("Matplotlib")
plt.xlabel("X ekseni")
plt.ylabel("Y ekseni")
plt.grid(True)
plt.xticks([0,1,2,3,4,5])

plt.legend()
plt.show()

fig, axes = plt.subplots(2,1, figsize=(9,7))
fig.subplots_adjust(hspace= 0.5)

x= [1,2,3,4,5,6,7,8,9,10]
y =[10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")


axes[1].scatter(y,x)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")



# random resim
plt.figure()
img = np.random.random((50,50))
plt.imshow(img, cmap ="gray") # 0= siyah 1=beyaz
#plt.axis("off")
plt.show()

# %% OS
import os

print(os.name)

currentDirc = os.getcwd()
print(currentDirc)

folder_name = "NewFolder"
os.mkdir(folder_name)