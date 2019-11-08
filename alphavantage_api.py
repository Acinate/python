import requests
import json
import time

base_url = "https://www.alphavantage.co/query?"
symbol = "WDC"
api_key = "JHGNBLAO8X1183MI"

intraday_url = base_url + "function=TIME_SERIES_INTRADAY&symbol="+symbol+"&interval=1min&outputsize=full&apikey="+api_key
sma_url = base_url + "function=SMA&symbol="+symbol+"&interval=1min&time_period=180&series_type=open&apikey="+api_key
ema_url = base_url + "function=EMA&symbol="+symbol+"&interval=1min&time_period=15&series_type=open&apikey="+api_key
vwap_url = base_url + "function=VWAP&symbol="+symbol+"&interval=1min&apikey="+api_key
macd_url = base_url + "function=MACD&symbol="+symbol+"&interval=1min&series_type=open&apikey="+api_key
rsi_url = base_url + "function=RSI&symbol="+symbol+"&interval=1min&time_period=14&series_type=open&apikey="+api_key
adx_url = base_url + "function=ADX&symbol="+symbol+"&interval=1min&time_period=100&apikey="+api_key


class AlphaApi:
    def __init__(self):
        self.datapoints = {}

    def get_datapoints(self):
        self.get_intraday_data()
        self.get_technicals()

    def get_intraday_data(self):
        url = intraday_url
        response = requests.get(url)
        json_response = response.json()
        intraday = json_response.get("Time Series (1min)")
        keys = intraday.keys()
        for key in keys:
            ts = intraday.get(key)
            dp = DataPoint(key)
            o = ts.get("1. open")
            h = ts.get("2. high")
            l = ts.get("3. low")
            c = ts.get("4. close")
            v = ts.get("5. volume")
            dp.add_intraday(o, h, l, c, v)
            self.datapoints[dp.time] = dp

    def get_technicals(self):
        urls = [sma_url, ema_url, vwap_url, macd_url, rsi_url, adx_url]
        technicals = ["SMA", "EMA", "VWAP", "MACD", "RSI", "ADX"]
        i = 0
        while i < len(urls):
            response = requests.get(urls[i])
            json_response = response.json()
            tech = json_response.get("Technical Analysis: " + technicals[i])
            if tech is None:
                print("Empty response, retrying in 10 seconds...")
                time.sleep(10)
            else:
                print("Getting Technical Indicator: " + technicals[i])
                keys = tech.keys()
                for key in keys:
                    t = tech.get(key)
                    v = t.get(technicals[i])
                    if self.datapoints.get(key) is not None:
                        self.datapoints.get(key).add_technical(technicals[i], v)
                i += 1


class DataPoint:
    def __init__(self, time):
        # 2019-10-31 15:49:00 (original)
        # 2019-10-31 15:49 (formatted)
        formatted_time = time[0:len(time) - 3]
        self.time = formatted_time
        self.open = None
        self.high = None
        self.low = None
        self.close = None
        self.volume = None
        self.sma = None
        self.ema = None
        self.vwap = None
        self.macd = None
        self.rsi = None
        self.adx = None

    def add_intraday(self, o, h, l, c, v):
        self.open = o
        self.high = h
        self.low = l
        self.close = c
        self.volume = v

    def add_technical(self, technical, value):
        if technical == "SMA":
            self.sma = value
        elif technical == "EMA":
            self.ema = value
        elif technical == "VWAP":
            self.vwap = value
        elif technical == "MACD":
            self.macd = value
        elif technical == "RSI":
            self.rsi = value
        elif technical == "ADX":
            self.adx = value

    def to_json(self):
        return json.dumps({
            'open': float(self.open) if self.open else None,
            'high': float(self.high) if self.high else None,
            'low': float(self.low) if self.low else None,
            'close': float(self.close) if self.close else None,
            'volume': float(self.volume) if self.volume else None,
            'sma': float(self.sma) if self.sma else None,
            'ema': float(self.ema) if self.ema else None,
            'vwap': float(self.vwap) if self.vwap else None,
            'macd': float(self.macd) if self.macd else None,
            'rsi': float(self.rsi) if self.rsi else None,
            'adx': float(self.adx) if self.adx else None
        })


class File:
    def __init__(self):
        self.filename = "datapoints.json"

    def write_datapoints_to_file(self, datapoints):
        fp = open(self.filename, "w")
        json_dictionary = json.dumps({k: v.__dict__ for k, v in datapoints.items()}, sort_keys=True, indent=4)
        fp.write(json_dictionary)
        print("Wrote results to file: " + self.filename)

    def read_datapoints_from_file(self):
        fp = open(self.filename, "r")
        datapoints = json.load(fp)
        return datapoints


class AlphaData:
    def __init__(self):
        self.datapoints = {}
        self.upper_band = None
        self.lower_band = None
        self.middle_band = None

    def get_alpha_data(self, datapoints):
        self.datapoints = datapoints
        self.find_upper_lower_bands()

    def find_upper_lower_bands(self):
        high_datapoint = None
        low_datapoint = None
        for key in self.datapoints.keys():
            if high_datapoint is None:
                if self.datapoints[key]["close"] is not None:
                    high_datapoint = self.datapoints[key]
            else:
                current = self.datapoints[key]["close"]
                if current is not None and current < high_datapoint["close"]:
                    high_datapoint = self.datapoints[key]
            if low_datapoint is None:
                if self.datapoints[key]["close"] is not None:
                    low_datapoint = self.datapoints[key]
            else:
                current = self.datapoints[key]["close"]
                if current is not None and current > low_datapoint["close"]:
                    low_datapoint = self.datapoints[key]
        self.upper_band = high_datapoint
        self.lower_band = low_datapoint
        self.middle_band = (float(high_datapoint["close"]) + float(low_datapoint["close"])) / 2
