from alpha.alpha_api import AlphaApi
from alpha.alpha_chart import AlphaChart
from alpha.alpha_file import AlphaFile
from simulation.random_simulator import RandomSimulator


# Scans datapoints from alphavantage api and writes them to file
def scan_datapoints(symbol):
    datapoints = AlphaApi(symbol).get_datapoints()
    file = AlphaFile(symbol)
    file.write_datapoints_to_csv(datapoints)


# Displays alphadata as a chart
def display_chart(symbol):
    chart = AlphaChart(symbol)
    chart.display_chart()


# Simulate buying and selling
def run_simulator(symbol):
    simulator = RandomSimulator(symbol)
    simulator.trade_randomly()


# scan_datapoints("AMZN")
# scan_datapoints("JNUG")
# scan_datapoints("JDST")
# scan_datapoints("UWT")
# display_chart("UWT")
# run_simulator("JNUG")

# price_chart = PriceChart("AMZN")
# price_chart.display_chart()

# plot_scatter("JNUG", "UWT", "JDST")

# jnug_profits, jdst_profits, amzn_profits = [], [], []
#
# jnug_sim = simulator = RandomSimulator("JNUG")
# jdst_sim = simulator = RandomSimulator("JDST")
# amzn_sim = simulator = RandomSimulator("AMZN")
# for i in range(1000):
#     jnug_profits.append(jnug_sim.trade_randomly())
#     jdst_profits.append(jdst_sim.trade_randomly())
#     amzn_profits.append(amzn_sim.trade_randomly())

print("done")
