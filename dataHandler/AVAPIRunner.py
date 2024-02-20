from dataHandler import AlphaVantageAPI
from trade import accountHandler
from OMS import alpaca
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
apiKey = "PK5MR88UMQBJQD0XQTAA"
secret = "NRmXCNwMM0EfIfxuTkiKV5cpNs7jtgUCTfTPJ4Ej"

#symbol, interval, endpoint, filePath = AlphaVantageAPI.get_data_handler_constructor_args()
#data_handler = AlphaVantageAPI.DataHandler(symbol, interval, endpoint, filePath)
#data_handler.getPriceDataCSV()


#api = alpaca.alpaca_trade_api.REST(api_version='v2', key_id=apiKey, secret_key=secret, base_url=APCA_API_BASE_URL)
#
#account = api.get_account()
#
#
#print(account)
#

symbol1 = "SPY"
interval1 = "30min"
month1 = "2000-01"
month2 = "2000-02"




AlphaVantageAPI.DataHandler.getPriceDataCSV("30min", "2000-03")
#AlphaVantageAPI.DataHandler.combineDataFrames(symbol1, interval1, month1=month1, month2=month2)



