from dataHandler import AlphaVantageAPI

symbol, interval, endpoint, filePath = AlphaVantageAPI.get_data_handler_constructor_args()
data_handler = AlphaVantageAPI.DataHandler(symbol, interval, endpoint, filePath)


data_handler.getPriceDataCSV()

