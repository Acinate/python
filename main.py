from alpha.alpha_api import AlphaApi, AlphaData
from simulator import Simulator
from alpha.alpha_chart import AlphaChart
from alpha.alpha_file import File


# Scans datapoints from alphavantage api and writes them to file
def scan_datapoints(symbol):
    datapoints = AlphaApi(symbol).get_datapoints()
    file = File()
    file.write_datapoints_to_file(datapoints, symbol)


# Reads datapoints from file and parses them into alphadata
def read_alphadata(symbol):
    file = File()
    datapoints = file.read_datapoints_from_file(symbol)
    return AlphaData(datapoints)


# Displays alphadata as a chart
def display_chart(symbol):
    chart = AlphaChart(read_alphadata(symbol))
    chart.display_chart()


# Simulate buying and selling
def run_simulator(symbol):
    alphadata = read_alphadata(symbol)
    simulator = Simulator(alphadata.datapoints)
    simulator.trade_randomly()


# scan_datapoints("JNUG")
# scan_datapoints("JDST")
# scan_datapoints("UWT")
# display_chart("JDST")
run_simulator("JDST")
