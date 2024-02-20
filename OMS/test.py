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



if __name__ == "__main__":
    csv_dir = 'csv_dir' # CHANGE THIS!
    symbol_list = ['SPY_30min_2000']
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = datetime.datetime(2000, 1, 1, 0, 0, 0)

    backtest = Backtest(
    csv_dir, symbol_list, initial_capital, heartbeat,
    start_date, HistoricCSVDataHandler, SimulatedExecutionHandler,
    Portfolio, MovingAverageCrossStrategy
    )
    backtest.simulate_trading()