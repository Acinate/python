import matplotlib.pyplot as plt

from alpha.alpha_file import AlphaFile


class AlphaChart:
    def __init__(self, symbol):
        self.df = None
        self.symbol = symbol
        self.load_chart_data()

    def load_chart_data(self):
        self.df = AlphaFile(self.symbol).read_datapoints_from_csv()

    def display_chart(self):
        # Plot Price Chart with EMA, SMA and VWAP
        ax = plt.subplot(211)
        plt.plot(self.df['Close'], label=self.symbol, color='black')
        plt.plot(self.df['SMA'], label='SMA', color='green')
        plt.plot(self.df['EMA'], label='EMA', color='cyan')
        plt.plot(self.df['VWAP'], label='VWAP', color='purple')
        plt.legend(loc=0)

        # Plot MACD
        ax = plt.subplot(212)
        ax.axhline(y=0, color='black')
        plt.plot(self.df['MACD'], label='MACD', color='black')
        plt.legend(loc=0)

        # Plot RSI
        # ax = plt.subplot(213)
        # ax.axhline(y=0, color='black')
        # plt.plot(self.df['RSI'], label='RSI', color='black')
        # plt.legend(loc=0)

        plt.show()
