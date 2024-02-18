from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


apiKey = "PKCHE8CZV9F5L2TOHZYM"
secret = "OgqQ3agnjOPDNs4xUHidP68zPBdRABMwwpXqDgpb"


def getApiKey():
    return apiKey


def getSecret():
    return apiKey


def tradingClient():
    return TradingClient('api-key', 'secret-key')