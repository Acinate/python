import requests
import json
import time


class AlphaApi:
    def __init__(self, symbol):
        self.datapoints = {}
        self.url = "https://www.alphavantage.co/query?function="
        self.key = "apikey=JHGNBLAO8X1183MI"
        self.quote_url = self.url + "TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=1min&outputsize=full&" + self.key
        self.sma_url = self.url + "SMA&symbol=" + symbol + "&interval=1min&time_period=180&series_type=open&" + self.key
        self.ema_url = self.url + "EMA&symbol=" + symbol + "&interval=1min&time_period=15&series_type=open&" + self.key
        self.vwap_url = self.url + "VWAP&symbol=" + symbol + "&interval=1min&" + self.key
        self.macd_url = self.url + "MACD&symbol=" + symbol + "&interval=1min&series_type=open&apikey=" + self.key
        self.rsi_url = self.url + "RSI&symbol=" + symbol + "&interval=1min&time_period=14&series_type=open&" + self.key
        self.adx_url = self.url + "ADX&symbol=" + symbol + "&interval=1min&time_period=100&" + self.key

    def scan_datapoints(self):
        self.get_datapoints()

    def get_datapoints(self):
        self.get_intraday_data()
        self.get_technicals()
        return self.datapoints

    def get_intraday_data(self):
        url = self.quote_url
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
        urls = [self.sma_url, self.ema_url, self.vwap_url, self.macd_url, self.rsi_url, self.adx_url]
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


class AlphaData:
    def __init__(self, datapoints):
        self.datapoints = datapoints


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
