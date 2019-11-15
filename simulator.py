import random
import math


def generate_random_signal():
    signal = round(random.uniform(-1, 1))
    if signal == -1:
        return "SELL"
    elif signal == 0:
        return "HOLD"
    else:
        return "BUY"


class Simulator:
    def __init__(self, datapoints):
        self.datapoints = datapoints
        self.balance = 10000  # total balance
        self.shares = 0  # total number of shares owned

    def print_datapoints(self):
        for key in self.datapoints.keys():
            date = self.datapoints[key]["times"]
            close = self.datapoints[key]["close"]
            print(date + ":" + close)

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
        for key in self.datapoints.keys():
            # cost of share at current datapoint
            cost = float(self.datapoints[key]["close"])
            # generate buy, hold or sell signal
            signal = generate_random_signal()
            # execute trade based on generated signal
            self.make_trade(signal, cost)
            last_price = cost

        # sell off remaining shares
        self.sell_all_shares(last_price, self.shares)
        # output results
        print("Balance: " + str(self.balance))
        print("Shares: " + str(self.shares))
        print("Profit: " + str(self.balance - 10000))
