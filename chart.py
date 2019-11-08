import matplotlib.pyplot as plt
import numpy as np


def plot_sin_chart_test():
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)

    fig, ax = plt.subplots()
    fig.suptitle('Trig Functions')
    ax.plot(x, y)

    plt.show()


def plot_price_chart_test():
    x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    y = [119.25, 124.54, 121.30, 122.50, 124.36]

    fig, ax = plt.subplots()
    fig.suptitle('Price History')
    ax.plot(x, y)

    plt.show()


plot_price_chart_test()