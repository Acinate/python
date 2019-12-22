import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=S&apikey=JHGNBLAO8X1183MI&datatype=csv&outputsize=full

# Set the stock symbol & company name
company_symbol = "TMUS"
company_name = "T-Mobile"

# Importing the training set
dataset_train = pd.read_csv('data/' + company_symbol + '_Stock_Price_Train.csv')

# Reverse rows (Data is stored in descending date, we need ascending)
dataset_train = dataset_train.reindex(index=dataset_train.index[::-1])
training_set = dataset_train.iloc[:, 1:2].values

# Scale the prices from 0 - 1
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Creating a data structure with n timesteps and 1 output
X_train = []
y_train = []

# Set the window size
window_size = 60

for i in range(window_size, dataset_train.shape[0]):
    X_train.append(training_set_scaled[i - window_size:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Part 2 - Building the RNN

# Initialising the RNN
regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

# Adding a second LSTM layer and some Dropout regularisation
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularisation
regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularisation
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))

# Adding the output layer
regressor.add(Dense(units=1))

# Compiling the RNN
regressor.compile(optimizer='adam', loss='mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, epochs=1, batch_size=32)

# Get real stock prices
dataset_test = pd.read_csv('data/' + company_symbol + '_Stock_Price_Test.csv')
dataset_test = dataset_test.reindex(index=dataset_test.index[::-1])
real_stock_price = dataset_test.iloc[:, 1:2].values

# Get predicted stock prices
dataset_total = pd.concat((dataset_train['open'], dataset_test['open']), axis=0)
# # e.g., dataset_total = 3192, dataset_test = 14, window = 60, dataset_total[3118].values
# inputs = dataset_total[len(dataset_total) - len(dataset_test) - window_size:].values
# inputs = inputs.reshape(-1, 1)
# inputs = sc.transform(inputs)
# X_test = []
# Add our test data to X_test
# for i in range(window_size, window_size + dataset_test.shape[0]):
#     X_test.append(inputs[i - window_size:i, 0])
# # Convert to [predicted_len] x [window_size] matrix
# X_test = np.array(X_test)
# X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
# predicted_stock_price = regressor.predict(X_test)
# predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# the datapoints we know
known_data = dataset_total[len(dataset_total) - window_size:].values
known_data = known_data.reshape(-1, 1)
known_data = sc.transform(known_data)

# predict the next 5 prices
predicted_values = []
for i in range(0, 5):
    combined_data = known_data[i:known_data.shape[0]]
    for pv in predicted_values:
        combined_data = np.concatenate((combined_data, np.array([pv])), axis=0)
    x_test = []
    for j in range(window_size, window_size + i):
        x_test.append(combined_data[j - window_size:j, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    # window_size = 60, window_size + i = 65
    # for j in range(window_size, window_size + i):
    #     X_test.append(known_data[i - window_size:i, 0])
    # X_test = np.array(X_test)
    # X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    psp = regressor.predict(x_test)
    # psp = sc.inverse_transform(psp)
    predicted_values.append(psp[psp.shape[0] - 1])

predicted_values = sc.inverse_transform(predicted_values)

print(predicted_values)

# Visualising the results
plt.plot(real_stock_price, color='red', label='Real ' + company_name + ' Stock Price')
plt.plot(predicted_stock_price, color='blue', label='Predicted ' + company_name + ' Stock Price')
plt.title(company_name + ' Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel(company_name + ' Stock Price')
plt.legend()
plt.show()
