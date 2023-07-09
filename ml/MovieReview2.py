# load movie review text data
from tensorflow.keras.datasets import imdb
(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)

# split train set with validation set
from sklearn.model_selection import train_test_split
train_input, val_input, train_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)

# truncate words count until 100
from tensorflow.keras.preprocessing.sequence import pad_sequences
train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)

# create LSTM model
from tensorflow import keras
# model = keras.Sequential()
# model.add(keras.layers.Embedding(500, 16, input_length=100))
# model.add(keras.layers.LSTM(8))
# model.add(keras.layers.Dense(1, activation='sigmoid'))
# model.summary()

# compile & train model
# rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
# model.compile(optimizer=rmsprop, loss='binary_crossentropy',
#               metrics=['accuracy'])
# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-lstm-model.h5',
#                                         save_best_only=True)
# early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
#                                         restore_best_weights=True)
# history = model.fit(train_seq, train_target, epochs=100, batch_size=64,
#                     validation_data=(val_seq, val_target),
#                     callbacks=[checkpoint_cb, early_stopping_cb])

# apply dropout to LSTM model
# model2 = keras.Sequential()
# model2.add(keras.layers.Embedding(500, 16, input_length=100))
# model2.add(keras.layers.LSTM(8, dropout=0.3))
# model2.add(keras.layers.Dense(1, activation='sigmoid'))

# compile & train model
# rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
# model2.compile(optimizer=rmsprop, loss='binary_crossentropy',
#               metrics=['accuracy'])
# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-lstm-model.h5',
#                                         save_best_only=True)
# early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
#                                         restore_best_weights=True)
# history = model2.fit(train_seq, train_target, epochs=100, batch_size=64,
#                     validation_data=(val_seq, val_target),
#                     callbacks=[checkpoint_cb, early_stopping_cb])

# connect 2 LSTM models
# model3 = keras.Sequential()
# model3.add(keras.layers.Embedding(500, 16, input_length=100))
# model3.add(keras.layers.LSTM(8, dropout=0.3, return_sequences=True))
# model3.add(keras.layers.LSTM(8, dropout=0.3))
# model3.add(keras.layers.Dense(1, activation='sigmoid'))
# model3.summary()

# compile & train model
# rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
# model3.compile(optimizer=rmsprop, loss='binary_crossentropy',
#               metrics=['accuracy'])
# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-2lstm-model.h5',
#                                         save_best_only=True)
# early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
#                                         restore_best_weights=True)
# history = model3.fit(train_seq, train_target, epochs=100, batch_size=64,
#                     validation_data=(val_seq, val_target),
#                     callbacks=[checkpoint_cb, early_stopping_cb])

# create GRU models
model4 = keras.Sequential()
model4.add(keras.layers.Embedding(500, 16, input_length=100))
model4.add(keras.layers.GRU(8))
model4.add(keras.layers.Dense(1, activation='sigmoid'))
model4.summary()

# compile & train model
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model4.compile(optimizer=rmsprop, loss='binary_crossentropy',
              metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-gru-model.h5',
                                        save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                        restore_best_weights=True)
history = model4.fit(train_seq, train_target, epochs=100, batch_size=64,
                    validation_data=(val_seq, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

# draw graph of train loss & validation loss
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

# verity result of train by test set
test_seq = pad_sequences(test_input, maxlen=100)
rnn_model = keras.models.load_model('best-2lstm-model.h5')
rnn_model.evaluate(test_seq, test_target)
