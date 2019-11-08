from alphavantage_api import File, AlphaApi


def scan_datapoints():
    api = AlphaApi()
    file = File()
    api.get_datapoints()
    datapoints = api.datapoints
    file.write_datapoints_to_file(datapoints)


def get_datapoints():
    file = File()
    return file.read_datapoints_from_file()


scan_datapoints()
dp = get_datapoints()
print(dp)
