import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class AlphaChart:
    def __init__(self, alphadata):
        self.alphadata = alphadata
        self.x = []
        self.y1 = []
        self.y2 = []
        self.y3 = []
        self.y4 = []
        self.y5 = []
        self.y6 = []

    def load_chart_axis(self):
        x_data = []  # dates
        y1_data = []  # closes
        y2_data = []  # sma
        y3_data = []  # ema
        y4_data = []  # upper_band
        y5_data = []  # lower_band
        y6_data = []  # middle_band

        datapoints = self.alphadata.datapoints
        for key in datapoints.keys():
            x_data.append(datapoints[key]["time"])
            y1_data.append(float(datapoints[key]["close"]))
            if datapoints[key]["sma"] is not None:
                y2_data.append(float(datapoints[key]["sma"]))
            else:
                y2_data.append(0)
            if datapoints[key]["ema"] is not None:
                y3_data.append(float(datapoints[key]["ema"]))
            else:
                y3_data.append(0)
            y4_data.append(float(self.alphadata.upper_band["close"]))
            y5_data.append(float(self.alphadata.lower_band["close"]))
            y6_data.append(self.alphadata.middle_band)

        data_range = 1200
        self.x = x_data[len(self.x) - data_range:len(self.x)-1]
        self.y1 = y1_data[len(self.y1) - data_range:len(self.y1) - 1]
        self.y2 = y2_data[len(self.y2) - data_range:len(self.y2) - 1]
        self.y3 = y3_data[len(self.y3) - data_range:len(self.y3) - 1]
        self.y4 = y4_data[len(self.y4) - data_range:len(self.y4) - 1]
        self.y5 = y5_data[len(self.y5) - data_range:len(self.y5) - 1]
        self.y6 = y6_data[len(self.y6) - data_range:len(self.y6) - 1]

    def display_chart(self):
        self.load_chart_axis()
        df = pd.DataFrame(index=self.x)
        df['AAPL'] = self.y1
        df['SMA'] = self.y2
        df['EMA'] = self.y3
        df['UpperBand'] = self.y4
        df['LowerBand'] = self.y5
        df['MiddleBand'] = self.y6
        plt.plot(df['AAPL'], label='AAPL', color='b')
        plt.plot(df['SMA'], label='SMA', color='g')
        plt.plot(df['EMA'], label='EMA', color='r')
        plt.plot(df['UpperBand'], label='Upper Band', color='y')
        plt.plot(df['LowerBand'], label='Lower Band', color='y')
        plt.plot(df['MiddleBand'], label="Middle Band", color='y')
        plt.legend(loc=0)
        plt.show()


def plot_sin_chart_test():
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(12, 6))
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
