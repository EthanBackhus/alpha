import requests
import csv
from datetime import datetime, timedelta
import mplfinance as mpf
import pandas as pd
import json
from datetime import datetime, timedelta

#api_key = "965E954TXP8KEFW0"

#API_KEY = "965E954TXP8KEFW0"
API_KEY = "59G5C0MEAHRCBFQJ"


symbol = "SPY"  # Example stock symbol (Apple Inc.)
interval = "60min"  # 5-minute interval for intraday data
#month="2023-11" 
endpoint = f"https://www.alphavantage.co/query"
filePath = "data/SPY"
currentMonth = "2024-01"

class DataHandler(object):

    def __init__(self, symbol, interval, endpoint, filepath):
        self.symbol = symbol
        self.interval = interval
        self.endpoint = endpoint
        self.filepath = filepath


    def getPriceData(symbol, interval, month, showData=False):
        priceDataRequest = requests.get(endpoint, params=getPriceParams(symbol, interval, month, API_KEY))
        priceData = priceDataRequest.json()

        if priceDataRequest.status_code == 200:
            priceData = priceDataRequest.json()

            closePricePath = filePath + "/SPY" + month + ".json"
            with open(closePricePath, 'w') as json_file:
                json.dump((priceData), json_file, indent=4)


            if showData:
                # Extract data for the candlestick chart
                ohlc_data = []
                for timestamp, values in priceData['Time Series (5min)'].items():
                    ohlc_data.append([timestamp, float(values["1. open"]), float(values["2. high"]), float(values["3. low"]), float(values["4. close"]), float(values["5. volume"])])

                # Reverse the order of OHLC data
                ohlc_data.reverse()

                # Create a DataFrame for the candlestick chart
                df = pd.DataFrame(ohlc_data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
                df['Date'] = pd.to_datetime(df['Date'])
                df.set_index('Date', inplace=True)

                # Plot the candlestick chart
                mpf.plot(df, type='candle')

                # Extract and save the 5-minute data to a CSV file
                with open('SPY_data.csv', 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])

                    for timestamp, values in priceData['Time Series (5min)'].items():
                        row = [timestamp, values["1. open"], values["2. high"], values["3. low"], values["4. close"], values["5. volume"]]
                        csv_writer.writerow(row)
                print('Data saved to SPY_data.csv')
        else:
            print(f'Error: {priceDataRequest.status_code} - {priceDataRequest.text}')


    def getPriceDataCSV(interval, currentMonth):
        response = requests.get(endpoint, params=getPriceParamsCSV(symbol, interval, currentMonth, API_KEY))
        data = response.text

        file_path = f"csv_dir/{symbol}_{interval}_{currentMonth}.csv"

        cleaned_data = "\n".join(line.strip() for line in data.strip().split("\n"))

        # Write some data to the file
        with open(file_path, 'w') as file:
            file.write(cleaned_data)
        




    def getRSIData(symbol, interval):
        rsiDataRequest = requests.get(endpoint, params=getRSIParams(symbol, interval, API_KEY))
        rsiData = rsiDataRequest.json()

        rsiSavePath = filePath + "/RSI.json"

        if rsiDataRequest.status_code == 200:
            rsiData = rsiDataRequest.json()

            with open(rsiSavePath, 'w') as json_file:
                json.dump((rsiData), json_file, indent=4)




    def getVWAPData(symbol, interval):
        vwapDataRequest = requests.get(endpoint, params=getVWAPParams(symbol, interval, API_KEY))
        vwapData = vwapDataRequest.json()

        vwapSavePath = filePath + "/VWAP.json"

        if vwapDataRequest.status_code == 200:
            vwapData = vwapDataRequest.json()

            with open(vwapSavePath, 'w') as json_file:
                json.dump((vwapData), json_file, indent=4)



    # delete lol
    def displayData():
        degree = 1  # Linear regression
        coefficients = np.polyfit(np.arange(len(df)), df['Close'], degree)
        line_of_best_fit = np.poly1d(coefficients)

        # Create a new figure for the candlestick chart
        fig, axes = mpf.plot(df, type='candle', returnfig=True)

        # Add the line of best fit to the existing axes
        axes[0].plot(df.index, line_of_best_fit(np.arange(len(df))), label='Line of Best Fit', color='red')

        # Customize chart settings as needed (e.g., legends, titles, labels)
        axes[0].set_ylabel('Price')
        axes[0].set_title('Candlestick Chart with Line of Best Fit')
        axes[0].legend()

        # Show the chart
        mpf.show()


    def combineYearOfDataFrames(symbol, interval, year):
        df1 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-01.csv')
        df2 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-02.csv')
        df3 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-03.csv')
        df4 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-04.csv')
        df5 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-05.csv')
        df6 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-06.csv')
        df7 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-07.csv')
        df8 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-08.csv')
        df9 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-09.csv')
        df10 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-10.csv')
        df11 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-11.csv')
        df12 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-12.csv')

        # Concatenate the DataFrames
        combined_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])

        # Sort the combined DataFrame by the 'timestamp' column
        combined_df.sort_values('timestamp', inplace=True)

        # Save the combined DataFrame to a new CSV file
        combined_df.to_csv(f'csv_dir/{symbol}_{interval}_{year}.csv', index=False)



    #def previousMonthUntilJan2000(startingMonth, counter):
    #    current_date = datetime.strptime(startingMonth, '%Y-%m')
    #
    #    while current_date >= datetime(2000, 1, 1) and counter < 23:
    #        counter = counter + 1
    #        print("Going to next month: " + str(current_date))
    #        yield current_date.strftime('%Y-%m')
    #        current_date -= timedelta(days=current_date.day)
    #        current_date -= timedelta(days=1)
    #
    #
    #
    #def processMonths(starting_month):
    #    counter = 0
    #    for month in previousMonthUntilJan2000(starting_month, counter):
    #        # Call another function here passing the month
    #        getPriceData(symbol, interval, month, False)
    #


def getPriceParams(symbol, interval, month, API_KEY):
    params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": symbol,
    "interval": interval,
    "apikey": API_KEY,
    "month": month,
    "extended_hours": "false",
    "outputsize": "full",
    }
    return params


def getPriceParamsCSV(symbol, interval, month, API_KEY):
    params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": symbol,
    "interval": interval,
    "apikey": API_KEY,
    "month": month,
    "extended_hours": "false",
    "outputsize": "full",
    "datatype":"csv"
    }
    return params


def getRSIParams(symbol, interval, API_KEY):
    params = {
    "function": "RSI",
    "symbol": symbol,
    "interval": interval,
    "apikey": API_KEY,
    "extended_hours":"false",
    "time_period": 60,
    "series_type": "close",
    "datatype": "json"
    }
    return params


def getVWAPParams(symbol, interval, API_KEY):
    params = {
    "function": "VWAP",
    "symbol": symbol,
    "interval": interval,
    "apikey": API_KEY,
    "datatype": "json"
    }
    return params


def get_data_handler_constructor_args():
    return symbol, interval, endpoint, filePath






