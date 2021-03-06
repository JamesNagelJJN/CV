from __future__ import absolute_import, division, print_function
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import random
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras import Sequential
from sklearn.model_selection import train_test_split


path_data_GT = r'\Users\James\Desktop\Datasets\fish'
path_data = r'\Users\James\Desktop\Datasets\GT'

class_names = ['Black Sea Sprat','Gilt-Head Bream',
               'Hourse Mackerel','Red Mullet','Red Sea Bream',
               'Sea Bass','Shrimp','Striped Red Mullet','Trout']

class_names_GT = ['Black Sea Sprat GT','Gilt-Head Bream GT',
               'Hourse Mackerel GT','Red Mullet GT','Red Sea Bream GT',
               'Sea Bass GT','Shrimp GT','Striped Red Mullet GT','Trout GT']

img_size = 30
img_size_list = []
batch_num = 42
epochs = 30

def load_images_from_folder(img_size,class_name,path_to_img):
    training_data = []
    X = []
    y = []
    for category in class_name:
        path = os.path.join(path_to_img,category)
        class_num = class_name.index(category)
        for img in os.listdir(path):
            img = cv2.imread(os.path.join(path, img))
            img = cv2.resize(img, (img_size,img_size), interpolation = cv2.INTER_AREA)
            training_data.append([img,class_num])
    for features,label in training_data:
        X.append(features)
        y.append(label)
    random.shuffle(training_data)
    return X,y


def cnn(batch_num, epochs, X, y):

    val_stats = []

    X = np.array(X)
    y = np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25)

    model = Sequential()

    model.add(Conv2D(32,(3,3), input_shape=(img_size,img_size,3), activation='relu'))
    model.add(MaxPooling2D(2,2))
    model.add(Conv2D(64,(1,1), input_shape=(img_size,img_size,3), activation='relu'))
    model.add(MaxPooling2D(2,2))
    model.add(Flatten())
    model.add(Dense(units=512, activation='relu'))
    model.add(Dense(units=256, activation='relu'))
    model.add(Dense(units=9, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_num, verbose=1, validation_data=(X_test,y_test))
    val_loss, val_acc = model.evaluate(X_test,y_test)
    val_stats.append([val_loss,val_acc])
    return (history, val_stats)

batch_list = []
accuracy_value = []
plotting = []
for i in range(5):
    X,y = load_images_from_folder(img_size,class_names,path_data)
    history, new_val_stats = cnn(batch_num, epochs,X,y)

    val_losses = []
    val_accuracy = []

    for w,v in new_val_stats:
        val_losses.append(w)
        val_accuracy.append(v)
    accuracy_value.append(max(val_accuracy))
    plt.plot(history.history['val_accuracy'], label=img_size)
    plotting.append(history.history['accuracy'])
    img_size_list.append(img_size)
    batch_list.append(batch_num)
    img_size += 10


handles, labels = plt.gca().get_legend_handles_labels()
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))


x_ticks = [0,5,10,15,20,25,30]
y_ticks = [0,0.25,0.5,0.75,1]
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.title('Accuracy of fish classification CNN RGB')
plt.legend(handles[::-1],labels[::-1], title='IMG_SIZE', loc='lower right')
plt.show()

plt.plot(plotting)
plt.show()
