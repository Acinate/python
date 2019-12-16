import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

from alpha.alpha_api import AlphaApi

# Stock Symbol
symbol = "MSFT"

# Import the training data
# Gets OHLCV Daily Values for Symbol
api = AlphaApi(symbol)
train_data = api.get_daily(symbol)

# Scale the data
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(train_data)

# Create a data structure with 60 timesteps and 1 output
x_train = []
y_train = []
for i in range(10, len(train_data)):
    x_train.append(training_set_scaled[i - 10:i, 0])
    y_train.append(training_set_scaled[i, 4])
x_train = np.array(x_train)
y_train = np.array(y_train)

# Reshape the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build the NN
regressor = Sequential()

# Add the first LTSM layer and some Dropout regularisation
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
regressor.add(Dropout(0.2))

# Add the second LSTM layer and some Dropout regularisation
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

# Add a third LSTM layer and some Dropout regularisation
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

# Add a fourth LSTM layer and some Dropout regularisation
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))

# Add the output layer
regressor.add(Dense(units=1))

# Compile the RNN
regressor.compile(optimizer='adam', loss='mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(x_train, y_train, epochs=100, batch_size=32)

# Plot data
ax = plt.subplot(211)
plt.plot(train_data[:, 0], train_data[:, 4])
plt.show()
