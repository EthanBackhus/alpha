from dataHandler import AlphaVantageAPI
from trade import accountHandler
from OMS import alpaca
import pandas as pd
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

symbol = "SPY"
interval = "30min"
month1 = "2000-01-2000-02-2000-03-2000-04-2000-05-2000-06-2000-07-2000-08"
month2 = "2000-09-2000-10-2000-11-2000-12"
year = "2003"


#AlphaVantageAPI.DataHandler.getPriceDataCSV("30min", "2004-01")
#AlphaVantageAPI.DataHandler.combineDataFrames(symbol1, interval1, month1=month1, month2=month2)



def getDataAndConcat():
    for i in range(1, 13):
        num_str = "{:02d}".format(i)
        AlphaVantageAPI.DataHandler.getPriceDataCSV("30min", f"2003-{num_str}")

    AlphaVantageAPI.DataHandler.combineYearOfDataFrames(symbol, interval, "2003")



#AlphaVantageAPI.DataHandler.combineYearOfDataFrames(symbol, interval, "2002")
#getDataAndConcat()
    
#df1 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-01.csv')
#df2 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-02.csv')
#df3 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-03.csv')
#df4 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-04.csv')
#df5 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-05.csv')
#df6 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-06.csv')
#df7 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-07.csv')
#df8 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-08.csv')
#df9 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-09.csv')
#df10 = pd.read_csv(f'csv_dir/{symbol}_{interval}_{year}-10.csv')


df1 = pd.read_csv(f'csv_dir/{symbol}_{interval}_2000.csv')
df2 = pd.read_csv(f'csv_dir/{symbol}_{interval}_2001.csv')
df3 = pd.read_csv(f'csv_dir/{symbol}_{interval}_2002.csv')
df4 = pd.read_csv(f'csv_dir/{symbol}_{interval}_2003.csv')

combined_df = pd.concat([df1, df2, df3, df4])
combined_df.sort_values('timestamp', inplace=True)
combined_df.to_csv(f'csv_dir/{symbol}_{interval}_2000-2003.csv', index=False)

# Concatenate the DataFrames
#combined_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10])
#
## Sort the combined DataFrame by the 'timestamp' column
#combined_df.sort_values('timestamp', inplace=True)
#
## Save the combined DataFrame to a new CSV file
#combined_df.to_csv(f'csv_dir/{symbol}_{interval}_{year}.csv', index=False)