from __future__ import print_function
import datetime
import numpy as np
import pandas as pd
import statsmodels.api as sm
from strategy import Strategy
from event import SignalEvent
from backtest import Backtest
from data import HistoricCSVDataHandler
from execution import SimulatedExecutionHandler
from portfolio import Portfolio
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    filemode='w',
    format='%(message)s'  # Log only the message without the INFO:root: prefix
)

support_levels = [491.49, 497.92]
resistance_levels = [501.83, 503.10]



class ColeStrat(Strategy):
    """
    Carries out a strategy in which bot trades off set supp and res levels.
    Triggers trade when it hits support. Profit line 4x from stop loss
    Indicators like fib and 100 and 200 EMA included.
    Look for trades around support, 50% FIB and above the 100 and 200 EMA
    """
    def __init__(
    self, bars, events, support=support_levels, resistance=resistance_levels, short_window = 400, long_window = 400
    ):
        """
        Initialises the ColeStrat.
        Parameters:
        bars - The DataHandler object that provides bar information
        events - The Event Queue object.
        support - Support lines
        resistance - resistance lines
        """
        self.bars = bars
        self.symbol_list = self.bars.symbol_list
        self.events = events
        self.support = support_levels
        self.resistance = resistance_levels
        self.short_window = short_window
        self.long_window = long_window

        # Set to True if a symbol is in the market
        self.bought = self._calculate_initial_bought()


    def set_support(self, levels):
        self.support = levels


    def set_resistance(self, levels):
        self.resistance = levels


    def _calculate_initial_bought(self):
        """
        Adds keys to the bought dictionary for all symbols and sets them to 'OUT'.
        """

        bought = {}
        for s in self.symbol_list:
            bought[s] = 'OUT'
        return bought
    

    def calculate_signals(self, event):
        """
        Generates a new set of signals based on the suport and resistance given to it
        Bot will look for trades around support, above 50% fib and 100 and 200 EMA
        Profit will be 4x the stop loss
        """
        if event.type == 'MARKET':
            for s in self.symbol_list:
                bars = self.bars.get_latest_bars_values(s, "close", N=self.long_window)
                bar_date = self.bars.get_latest_bar_datetime(s)
            if bars is not None and len(bars) > 0:
                bars_series = pd.Series(bars)
                ema_100 = bars_series.ewm(span=100, adjust=False).mean()
                ema_200 = bars_series.ewm(span=200, adjust=False).mean()

                symbol = s
                dt = datetime.datetime.utcnow()
                sig_dir = ""

                #print(bars)


    def test(self, event):
        """
        Generates a new set of signals based on the MAC
        SMA with the short window crossing the long window
        meaning a long entry and vice versa for a short entry.
        Parameters
        event - A MarketEvent object.
        """
        if event.type == 'MARKET':
            for s in self.symbol_list:
                bars = self.bars.get_latest_bars_values(s, "close", N=self.long_window)
                bar_date = self.bars.get_latest_bar_datetime(s)
            if bars is not None and len(bars) > 0:
                short_sma = np.mean(bars[-self.short_window:])
                long_sma = np.mean(bars[-self.long_window:])

                symbol = s
                dt = datetime.datetime.utcnow()
                sig_dir = ""

                if short_sma > long_sma and self.bought[s] == "OUT":
                    print("LONG: %s" % bar_date)
                    sig_dir = 'LONG'
                    signal = SignalEvent(1, symbol, dt, sig_dir, 1.0)
                    self.events.put(signal)
                    self.bought[s] = 'LONG'
                elif short_sma < long_sma and self.bought[s] == "LONG":
                    print("SHORT: %s" % bar_date)
                    sig_dir = 'EXIT'
                    signal = SignalEvent(1, symbol, dt, sig_dir, 1.0)
                    self.events.put(signal)
                    self.bought[s] = 'OUT'











if __name__ == "__main__":
    csv_dir = 'csv_dir' # CHANGE THIS!
    symbol_list = ['SPY_30min_2024-01-02']
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = datetime.datetime(2024, 1, 1, 0, 0, 0)

    backtest = Backtest(
    csv_dir, symbol_list, initial_capital, heartbeat,
    start_date, HistoricCSVDataHandler, SimulatedExecutionHandler,
    Portfolio, ColeStrat
    )
    backtest.simulate_trading()