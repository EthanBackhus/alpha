from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
import alpaca_trade_api
from config import config

trading_client = TradingClient(config.getApiKey(), config.getSecret())
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
apiKey = "PK5MR88UMQBJQD0XQTAA"
secret = "NRmXCNwMM0EfIfxuTkiKV5cpNs7jtgUCTfTPJ4Ej"



class AlpacaHandler(object):

    def __init__(self):
        self.apiKey = apiKey
        self.secret = secret
        self.trading_client = TradingClient(api_key=apiKey, secret_key=secret)
        self.tradeapi = alpaca_trade_api.REST(api_version='v2', api_key=apiKey, secret_key=secret)


    