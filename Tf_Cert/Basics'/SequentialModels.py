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
Seq_model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

Seq_model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

Seq_model.fit(
    train_images,train_labels,epochs=5,verbose=2,batch_size=batch_size
)

Seq_model.evaluate(
    test_images,test_labels,verbose=1
)

