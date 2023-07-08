# load movie review text data
from tensorflow.keras.datasets import imdb
(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
print(train_input.shape, test_input.shape) # sample count of train set & test set
print(len(train_input[0]), len(train_input[1])) # words count of 1st & 2nd samples
print(train_input[0]) # tonken list of 1st sample
print(train_target[:20]) # target data

# divide train set with validation set
from sklearn.model_selection import train_test_split
train_input, val_input, train_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)
# get words count of each review
import numpy as np
lengths = np.array([len(x) for x in train_input])
print(np.mean(lengths), np.median(lengths))

import matplotlib.pyplot as plt
plt.hist(lengths)
plt.xlabel('length')
plt.ylabel('frequency')
plt.show()

# truncate words count until 100
from tensorflow.keras.preprocessing.sequence import pad_sequences
train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)
print(train_seq.shape) # sample count of new train set
print(train_seq[0]) # token list of 1st sample
print(train_seq[5]) # token list of 6st sample

# transform train set by one-hot incoding
from tensorflow import keras
# train_oh = keras.utils.to_categorical(train_seq)
# val_oh = keras.utils.to_categorical(val_seq)
# print(train_oh.shape) # shape of train set
# print(train_oh[0][0][:20]) # content of 1st sample

# create Recurrent Nural Network by One-Hot incoding
# model = keras.Sequential()
# model.add(keras.layers.SimpleRNN(8, input_shape=(100, 500)))
# model.add(keras.layers.Dense(1, activation='sigmoid'))
# model.summary()

# compile & train model
# rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
# model.compile(optimizer=rmsprop, loss='binary_crossentropy',
#               metrics=['accuracy'])
# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5',
#                                         save_best_only=True)
# early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
#                                         restore_best_weights=True)
# history = model.fit(train_oh, train_target, epochs=100, batch_size=64,
#                     validation_data=(val_oh, val_target),
#                     callbacks=[checkpoint_cb, early_stopping_cb])

# draw graph of train loss & validation loss
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend(['train', 'val'])
# plt.show()

# create Recurrent Nural Network by Word embedding
model2 = keras.Sequential()
model2.add(keras.layers.Embedding(500, 16, input_length=100))
model2.add(keras.layers.SimpleRNN(8))
model2.add(keras.layers.Dense(1, activation='sigmoid'))
model2.summary()

# compile & train model
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model2.compile(optimizer=rmsprop, loss='binary_crossentropy',
              metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-embedding-model.h5',
                                        save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3,
                                        restore_best_weights=True)
history = model2.fit(train_seq, train_target, epochs=100, batch_size=64,
                    validation_data=(val_seq, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

# draw graph of train loss & validation loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()
