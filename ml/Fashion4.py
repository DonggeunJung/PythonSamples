# load fashion image data
from tensorflow import keras

(train_input, train_target), (test_input, test_target) =\
    keras.datasets.fashion_mnist.load_data()

# scale & transform to 1 dimension
from sklearn.model_selection import train_test_split
train_scaled = train_input.reshape(-1, 28, 28, 1) / 255.0
train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# create convolution nuran network
model = keras.Sequential()
model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu',
                             padding='same', input_shape=(28,28,1)))
model.add(keras.layers.MaxPool2D(2))
model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu',
                              padding='same'))
model.add(keras.layers.MaxPool2D(2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
keras.layers.Dropout(0.3)
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()
keras.utils.plot_model(model, show_shapes=True)

# compile & train model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5',
                                        save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                        restore_best_weights=True)
history = model.fit(train_scaled, train_target, epochs=20,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

# loss graph of train set & validate set
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

# 1st sample of validate set
plt.imshow(val_scaled[0].reshape(28, 28), cmap='gray_r')
plt.show()
# predict 1st sample of validate set
preds = model.predict(val_scaled[0:1])
print(preds)
classes = ['t-shirts', 'pants', 'sweater', 'dress', 'coat',
           'sandals', 'shirts', 'sneakers', 'bag', 'boots']
import numpy as np
print(classes[np.argmax(preds)])

# check performance by test set
test_scaled = test_input.reshape(-1, 28, 28, 1) / 255.0
model.evaluate(test_scaled, test_target)
