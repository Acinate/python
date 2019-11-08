from alphavantage_api import File, AlphaApi, AlphaData
from chart import AlphaChart


def scan_datapoints():
    api = AlphaApi()
    file = File()
    api.get_datapoints()
    datapoints = api.datapoints
    file.write_datapoints_to_file(datapoints)


def get_datapoints():
    file = File()
    return file.read_datapoints_from_file()


def get_alphadata():
    datapoints = get_datapoints()
    alphadata = AlphaData()
    alphadata.get_alpha_data(datapoints)
    return alphadata


# scan_datapoints()
alphadata = get_alphadata()
alphachart = AlphaChart(alphadata)
alphachart.display_chart()
