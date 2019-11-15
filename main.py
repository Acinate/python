from alphavantage_api import File, AlphaApi, AlphaData
from simulator import Simulator
from alpha_chart import AlphaChart


# Scans datapoints from alphavantage api and writes them to file
def scan_datapoints(symbol):
    datapoints = AlphaApi("TSLA").get_datapoints()
    file = File()
    file.write_datapoints_to_file(datapoints)


# Reads datapoints from file and parses them into alphadata
def read_alphadata():
    file = File()
    datapoints = file.read_datapoints_from_file()
    return AlphaData(datapoints)


# Displays alphadata as a chart
def display_chart():
    chart = AlphaChart(read_alphadata())
    chart.display_chart()


# Simulate buying and selling
def run_simulator():
    alphadata = read_alphadata()
    simulator = Simulator(alphadata.datapoints)
    simulator.trade_randomly()


# scan_datapoints("AAPL")
# display_chart()
run_simulator()
