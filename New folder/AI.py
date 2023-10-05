# 1. load dữ liệu và chia train, val, test

import numpy
from keras.layers import Dense
from keras import Sequential
from keras.models import load_model
from numpy import loadtxt
from sklearn.model_selection import train_test_split
dataset = loadtxt('pima.csv', delimiter=",")

x= dataset[:,0:8]
y = dataset[:,8]

x_train_val, x_test, y_train_val, y_test = train_test_split(x, y, test_size=0.2)
x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.2)

# model = Sequential()
# model.add(Dense(16,input_dim=8, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# model.fit(x_train, y_train, epochs=100, batch_size=8, validation_data=(x_val, y_val))

# model.save("mymodel.h5")
model = load_model('mymodel.h5')

loss, acc = model.evaluate(x_test, y_test)
print('loss = ', loss )
print('accuracy = ',acc)

x_new = x_test[10]
y_new = y_test[10]
y_predict = model.predict(x_new)


x_new = numpy.expand_dims(x_new, axis=0)



print("gia tri du don la = ", y_predict)
print('gia tri thuc te la', y_new)