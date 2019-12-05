import matplotlib.pyplot as plt
import pandas as pd


class AlphaChart:
    def __init__(self, alphadata):
        self.alphadata = alphadata
        self.x_date = []
        self.y_close = []
        self.y_sma = []
        self.y_ema = []
        self.y_macd = []
        self.y_rsi = []
        self.y_vwap = []

    def load_chart_axis(self):
        datapoints = self.alphadata.datapoints
        for key in datapoints.keys():
            datapoint = datapoints[key]
            self.x_date.append(datapoint["time"])
            self.y_close.append(float(datapoint["close"]))
            self.y_sma.append(float(datapoint["sma"]))
            self.y_ema.append(float(datapoint["ema"]))
            self.y_macd.append(float(datapoint["macd"]))
            self.y_rsi.append(float(datapoint["rsi"]))
            self.y_vwap.append(float(datapoint["vwap"]))

    def display_chart(self):
        self.load_chart_axis()
        df = pd.DataFrame(index=self.x_date)
        df['Price'] = self.y_close
        df['SMA'] = self.y_sma
        df['EMA'] = self.y_ema
        df['MACD'] = self.y_macd
        df['RSI'] = self.y_rsi
        df['VWAP'] = self.y_vwap

        # Plot Price Chart with EMA, SMA and VWAP
        ax = plt.subplot(211)
        plt.plot(df['Price'], label='Price', color='blue')
        plt.plot(df['SMA'], label='SMA', color='green')
        plt.plot(df['EMA'], label='EMA', color='cyan')
        plt.plot(df['VWAP'], label='VWAP', color='purple')
        plt.legend(loc=0)

        # Plot MACD
        ax = plt.subplot(212)
        ax.axhline(y=0, color='black')
        plt.plot(df['MACD'], label='MACD', color='black')
        plt.legend(loc=0)

        # Plot RSI
        # ax = plt.subplot(213)
        # ax.axhline(y=0, color='black')
        # plt.plot(df['RSI'], label='RSI', color='black')
        # plt.legend(loc=0)

        plt.show()
