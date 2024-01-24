import os

import numpy as np
import tensorflow as tf

print(tf.__version__)

train_path = '/home/kalyan/DataSets/dataset/training_set/'
test_path = '/home/kalyan/DataSets/dataset/test_set/'


train_dogs = train_path +'dogs'
train_cats = train_path + 'cats'

test_dogs = test_path + 'dogs'
test_cats = test_path + 'cats'


img_width = 128
img_height = 128
img_size = (img_width,img_height)
img_chan = 3


num_cat_img = len(os.listdir((train_cats)))
print(num_cat_img)
num_dog =  len(os.listdir((train_dogs)))
print(num_dog)


#data_aug
data_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=(1/255.0),
                                                           validation_split=0.2)

train_data = data_gen.flow_from_directory(
    train_path,
    target_size=img_size,
    batch_size=32,
    subset='training',
    class_mode='binary'
)

val_data = data_gen.flow_from_directory(
    train_path,
    target_size=img_size,
    batch_size=32,
    subset='validation',
    class_mode='binary'
)


images,labels = train_data.next()
print(len(images)),print(len(labels)), print(images[0].shape)

train_data,val_data

# model
cnn = tf.keras.models.Sequential([
    tf.keras.Input(shape=images[0].shape),
    tf.keras.layers.Conv2D(32,(3,3),padding='same',activation='relu'),
    tf.keras.layers.MaxPool2D((2,2),strides=2),
    tf.keras.layers.Conv2D(64,(3,3),padding='same',activation='relu'),
    tf.keras.layers.MaxPool2D((2,2),strides=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

cnn.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

cnn.summary()

#callbacks
reducelearninRate = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_accuracy',
                                                         patience=3,
                                                         verbose=1,
                                                         factor=0.5,
                                                         min_lr=0.00001)

cnn.fit(
    train_data,
    batch_size=32,
    epochs=3,
    validation_data=val_data,
    verbose=1,
    callbacks= [reducelearninRate]
)


def preprocess_images(path):
    img = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))

    img_array = tf.keras.preprocessing.image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_preprocessed = img_array / 255.0

    return img_preprocessed

img_path = train_dogs + "/dog.4005.jpg"
img = preprocess_images(img_path)
prediction = cnn.predict(img)

predicted_class_index = np.argmax(prediction)

class_labels = ['cats', 'dogs']
predicted_class_label = class_labels[predicted_class_index]

print("Predicted class:", predicted_class_label)