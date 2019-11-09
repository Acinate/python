import matplotlib.pyplot as plt
import pandas as pd


class AlphaChart:
    def __init__(self, alphadata):
        self.alphadata = alphadata
        self.x_date = []
        self.y_close = []
        self.y_sma = []
        self.y_ema = []
        self.y_sma_close = []
        self.y_upper_band = alphadata.upper_band
        self.y_lower_band = alphadata.lower_band
        self.y_middle_band = alphadata.middle_band
        self.y_middle_band_close = []

    def load_chart_axis(self):
        datapoints = self.alphadata.datapoints
        for key in datapoints.keys():
            datapoint = datapoints[key]
            self.x_date.append(datapoint["time"])
            self.y_close.append(float(datapoint["close"]))
            self.y_sma.append(float(datapoint["sma"]))
            self.y_ema.append(float(datapoint["ema"]))
            self.y_sma_close.append(float(datapoint["sma"]) - float(datapoint["close"]))
            self.y_middle_band_close.append(float(datapoint["close"]) - self.alphadata.middle_band)

    def display_chart(self):
        self.load_chart_axis()
        df = pd.DataFrame(index=self.x_date)
        df['AAPL'] = self.y_close
        df['SMA'] = self.y_sma
        df['EMA'] = self.y_ema
        df['SMA - Close'] = self.y_sma_close
        df['MB - Close'] = self.y_middle_band_close
        ax = plt.subplot(211)
        ax.axhline(y=self.y_upper_band, color='y')
        ax.axhline(y=self.y_middle_band, color='y')
        ax.axhline(y=self.y_lower_band, color='y')
        plt.plot(df['AAPL'], label='AAPL', color='b')
        plt.plot(df['SMA'], label='SMA', color='g')
        plt.plot(df['EMA'], label='EMA', color='r')
        plt.legend(loc=0)

        ax = plt.subplot(212)
        ax.axhline(y=0, color='y')
        plt.plot(df['SMA - Close'], label='SMA Difference', color='b')
        plt.plot(df['MB - Close'], label='Middle Band Difference', color='r')
        plt.legend(loc=0)
        plt.show()
