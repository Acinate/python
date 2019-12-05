import json


class File:
    def __init__(self):
        self.filename = "unknown_datapoints.json"
        self.directory = "data/"

    def write_datapoints_to_file(self, datapoints, symbol):
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

    def write_datapoints_to_csv(self, datapoints, symbol):
        self.filename = self.directory + symbol + "_datapoints.csv"
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
        for line in lines:
            fp.write(line + "\n")
        print("Wrote results to file: " + self.filename)


def read_datapoints_from_file(self, symbol):
    self.filename = self.directory + symbol + "_datapoints.json"
    fp = open(self.filename, "r")
    datapoints = json.load(fp)
    return datapoints
