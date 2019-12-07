import math

import numpy as np


# prints formatted price
def formatPrice(n):
    return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))


# returns the sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# returns an an n-day state representation ending at time t
def getState(data, t, n):
    d = t - n + 1
    block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1]  # pad with t0
    res = []
    for i in range(n - 1):
        res.append(sigmoid(block[i + 1][0] - block[i][0]))
    return np.array([res])


# formats alpha data into array of indicators
def formatAlphaData(data):
    formatted = []
    for i in range(data.shape[0]):
        formatted.append(data.iloc[i].values[1:].tolist())
    return formatted
