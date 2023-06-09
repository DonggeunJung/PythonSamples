# load fashion image data
from tensorflow import keras

(train_input, train_target), (test_input, test_target) =\
    keras.datasets.fashion_mnist.load_data()

# scale & transform to 1 dimension
from sklearn.model_selection import train_test_split
train_scaled = train_input / 255.0
# train_scaled = train_scaled.reshape(-1, 28*28)
train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# add hidden layer
# dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(28*28,),
#                             name='hidden')
# dense2 = keras.layers.Dense(10, activation='softmax', name='output')
# model = keras.Sequential([dense1, dense2], name='Fashion_MNIST')

# use ReLU method for hidden layer
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
model.summary()

# train image data by keras
# model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)

# check result of train
model.evaluate(val_scaled, val_target)
