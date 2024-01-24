import tensorflow as tf

print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

#resizing
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)) /255.0
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)) / 255.0

#1hot enco
train_labels = tf.keras.utils.to_categorical(train_labels,num_classes=10)
test_labels = tf.keras.utils.to_categorical(test_labels,num_classes=10)

batch_size = 32
Conv_model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',kernel_initializer='he_uniform',input_shape=(28,28,1)),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(100,activation='relu',kernel_initializer='he_uniform'),
    tf.keras.layers.Dense(10,activation='softmax')
])

Conv_model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

Conv_model.fit(
    train_images,train_labels,epochs=5,verbose=1
)
Conv_model.evaluate(
    test_images,test_labels,verbose=2
)