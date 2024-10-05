import pandas as pd
import csv
import dash
print(dash.__version__)


import pandas as pd 


df = pd.concat(
    [pd.read_csv(file, usecols=['product','price','quantity','date','region']) for file in ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']],
    ignore_index=True
)
df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
df['sales'] = df['price'] * df['quantity']


pink_morsel = df[df['product'].str.contains('pink morsel', case=False, na=False)]


print(pink_morsel[['product','sales','date','region']])


