from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from config import config

trading_client = TradingClient(config.getApiKey(), config.getSecret())

def checkAccountDetails():
    account = trading_client.get_account()

    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print('Account is currently restricted from trading.')

    # Check how much money we can use to open new positions.
    print('${} is available as buying power.'.format(account.buying_power))


