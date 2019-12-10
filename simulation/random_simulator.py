import math
import random

from alpha.alpha_file import AlphaFile


def generate_random_signal():
    signal = round(random.uniform(-1, 1))
    if signal == -1:
        return "SELL"
    elif signal == 0:
        return "HOLD"
    else:
        return "BUY"


class RandomSimulator:
    def __init__(self, symbol):
        self.symbol = symbol
        self.df = AlphaFile(symbol).read_datapoints_from_csv()
        self.balance = 10000  # total balance
        self.shares = 0  # total number of shares owned
        self.profit = 0  # new balance minus original balance

    def purchase_shares(self, cost):
        # calculate max number of shares we can purchase
        max_shares = math.floor(self.balance / cost)
        # generate random number of shares between 1 and max_shares
        shares = round(random.uniform(1, max_shares))
        # purchase the shares (subject balance from shares * cost)
        self.balance = self.balance - (shares * cost)
        # update the number of shares we own
        self.shares = self.shares + shares

    def sell_shares(self, cost):
        # generate random number of shares between 1 and shares
        shares = round(random.uniform(1, self.shares))
        self.sell_all_shares(cost, shares)

    def sell_all_shares(self, cost, shares):
        # update balance
        self.balance = self.balance + (shares * cost)
        # update shares we own
        self.shares = self.shares - shares

    def make_trade(self, signal, share_cost):
        if signal == "BUY":
            # check if we have enough balance to make buy a position
            if self.balance >= share_cost:
                self.purchase_shares(share_cost)
        elif signal == "SELL":
            # check if we have shares to sell
            if self.shares > 0:
                self.sell_shares(share_cost)

    def trade_randomly(self):
        last_price = None
        for close in self.df['Close'].values:
            # cost of share at current datapoint
            cost = close
            # generate buy, hold or sell signal
            signal = generate_random_signal()
            # execute trade based on generated signal
            self.make_trade(signal, cost)
            last_price = cost

        # sell off remaining shares
        self.sell_all_shares(last_price, self.shares)

        # calculate profit
        self.profit = self.balance - 10000

        # output results
        # print("Balance: " + str(self.balance))
        # print("Shares: " + str(self.shares))
        # print("Profit: " + str(self.balance - 10000))

        return self.profit
