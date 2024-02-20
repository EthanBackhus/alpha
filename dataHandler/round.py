import pandas as pd


df = pd.read_csv('csv_dir/SPY_30mins_2024-01-02.csv')

df = df.round(3)

df.to_csv('csv_dir/SPY_30mins_2024-01-02.csv', index=False)