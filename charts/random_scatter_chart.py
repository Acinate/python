from simulation.random_simulator import RandomSimulator


# This file plots a scatter chart based on random trades to identify trends in the three different chart patterns.


def plot_scatter(asc_symbol, hor_symbol, desc_symbol):
    # Initialize array of profits
    asc_arr, hor_arr, desc_arr = [], [], []

    for i in range(100):
        asc_arr.append(RandomSimulator(asc_symbol).trade_randomly())
        hor_arr.append(RandomSimulator(hor_symbol).trade_randomly())
        desc_arr.append(RandomSimulator(desc_symbol).trade_randomly())

    print(asc_arr)
    print(hor_arr)
    print(desc_arr)
