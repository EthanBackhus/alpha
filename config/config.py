from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


apiKey = "PK5MR88UMQBJQD0XQTAA"
secret = "NRmXCNwMM0EfIfxuTkiKV5cpNs7jtgUCTfTPJ4Ej"


def getApiKey():
    return apiKey


def getSecret():
    return apiKey


def tradingClient():
    return TradingClient('api-key', 'secret-key')