import json

import pandas as pd


class AlphaFile:
    def __init__(self, symbol):
        self.filename = symbol + "_datapoints.csv"
        self.directory = "data/"

    def write_datapoints_to_csv(self, datapoints):
        self.filename = self.directory + self.filename
        lines = []
        for key in datapoints.keys():
            datapoint = datapoints[key]
            if datapoint.sma is not None \
                    and datapoint.ema is not None \
                    and datapoint.vwap is not None \
                    and datapoint.macd is not None \
                    and datapoint.rsi is not None \
                    and datapoint.adx is not None:
                line = key + "," + \
                       datapoint.close + "," + \
                       datapoint.sma + "," + \
                       datapoint.ema + "," + \
                       datapoint.vwap + "," + \
                       datapoint.macd + "," + \
                       datapoint.rsi + "," + \
                       datapoint.adx
                lines.append(line)
        fp = open(self.filename, "w")
        for line in reversed(lines):
            fp.write(line + "\n")
        print("Wrote results to file: " + self.filename)

    def read_datapoints_from_csv(self):
        return pd.read_csv(self.directory + self.filename,
                           names=['Date', 'Close', 'SMA', 'EMA', 'VWAP', 'MACD', 'RSI', 'ADX'])

    def write_datapoints_to_json(self, datapoints, symbol):
        self.filename = self.directory + symbol + "_datapoints.json"
        good_datapoints = {}
        for key in datapoints.keys():
            datapoint = datapoints[key]
            if datapoint.sma is not None \
                    and datapoint.ema is not None \
                    and datapoint.vwap is not None \
                    and datapoint.macd is not None \
                    and datapoint.rsi is not None \
                    and datapoint.adx is not None:
                good_datapoints[key] = datapoint
        fp = open(self.filename, "w")
        json_dictionary = json.dumps({k: v.__dict__ for k, v in good_datapoints.items()}, sort_keys=True, indent=4)
        fp.write(json_dictionary)
        print("Wrote results to file: " + self.filename)

    def read_datapoints_from_json(self, symbol):
        self.filename = self.directory + symbol + "_datapoints.json"
        fp = open(self.filename, "r")
        datapoints = json.load(fp)
        return datapoints
