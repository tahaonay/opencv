import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D,Flatten, Dropout, BatchNormalization
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
import pickle
from sklearn.metrics import confusion_matrix

path = "Dataset"
numofclass = len(os.listdir(path))
print(numofclass)

images = []
classNo= []   # which number 0-9

for i in range(numofclass):  # 0-9
    myImageList = os.listdir(path + "\\" + str(i))
    for j in myImageList:
        img = cv2.imread(path + "\\" + str(i) + "\\" + j)
        img = cv2.resize(img, (32,32))
        images.append(img)    # images
        classNo.append(i)     # number class of image


print("Number of İmages: " , len(images))
print("Items of class: ",len(classNo))

images = np.array(images)
classNo = np.array(classNo)

print(images.shape)
print(classNo.shape)


# (0.5 test, 0.5 train) >>(0.5 test, 0.25 train,0.25 validation)
x_train,x_test,y_train,y_test = train_test_split(images,classNo,test_size=0.5,random_state=42)
x_train,x_validation,y_train,y_validation = train_test_split(x_train,y_train,test_size=0.2,random_state=42)

print(images.shape)
print(x_train.shape)
print(x_test.shape)
print(x_validation.shape)

"""
#visualition
fig, axes = plt.subplots(3,1,figsize=(7,7))
fig.subplots_adjust(hspace = 0.5)

sns.countplot(y_train, ax= axes[0])
axes[0].set_title("y_train")

sns.countplot(y_test, ax= axes[1])
axes[1].set_title("y_test")

sns.countplot(y_validation, ax= axes[2])
axes[2].set_title("y_validation")
"""

#preprocession
def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    
    return img


""" for test
ind = 50
img = preProcess(x_train[ind])
img = cv2.resize(img,(300,300))
cv2.imshow("Preprocess",img)
"""

x_train = np.array(list(map(preProcess,x_train)))
x_test = np.array(list(map(preProcess,x_test)))
x_validation = np.array(list(map(preProcess,x_validation)))

x_train = x_train.reshape(-1,32,32,1)
x_test = x_test.reshape(-1,32,32,1)
x_validation = x_validation.reshape(-1,32,32,1)


# data generation

dataGen = ImageDataGenerator(width_shift_range= 0.1,
                             height_shift_range= 0.1,
                             zoom_range= 0.1,
                             rotation_range=10)

dataGen.fit(x_train)

y_train = to_categorical(y_train, numofclass)
y_test = to_categorical(y_test, numofclass)
y_validation = to_categorical(y_validation, numofclass)



model = Sequential()
model.add(Conv2D(input_shape = (32,32,1),filters=8, kernel_size= (5,5), activation="relu",padding="same"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(filters=16, kernel_size= (3,3), activation="relu",padding="same"))
model.add(MaxPooling2D(pool_size = (2,2)))


model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(units=256,activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(units=numofclass,activation="softmax"))

model.compile(loss = "categorical_crossentropy",optimizer=("Adam"), metrics=["accuracy"])

batch_size = 250
hist = model.fit_generator(dataGen.flow(x_train,y_train,batch_size=batch_size),
                                        validation_data = (x_validation,y_validation),
                                        epochs=15, steps_per_epoch = x_train.shape[0]//batch_size, shuffle =1)

pickle_out = open("model_trained_new.p","wb")
pickle.dump(model,pickle_out)
pickle_out.close()

# %% 

hist.history.keys()

plt.figure()
plt.plot(hist.history["loss"],label=("Teach loss"))
plt.plot(hist.history["val_loss"],label=("Val Loss"))
plt.legend()
plt.show()

plt.figure()
plt.plot(hist.history["accuracy"],label=("accuracy"))
plt.plot(hist.history["val_accuracy"],label=("Val accuracy"))
plt.legend()
plt.show()

score = model.evaluate(x_test, y_test,verbose =1)
print("test loss: ",score[0])
print("test accuracy: ",score[1])

y_pred = model.predict(x_validation)

y_pred_class = np.argmax(y_pred,axis = 1)
y_true = np.argmax(y_validation, axis =1)

cm= confusion_matrix(y_true, y_pred_class)
f, ax = plt.subplots(figsize =(8,8))
sns.heatmap(cm,annot=True,linewidth =0.01,cmap="Greens", linecolor="gray",fmt=".1f",ax=ax)
plt.xlabel=("predicted")
plt.ylabel=("true")
plt.title("cm")
plt.show


