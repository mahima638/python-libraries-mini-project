import pandas as pd
import datetime
#df= pd.read_csv('time_series.csv')
#print(df.head())
#print(df.dtypes)
#df.Datetime = pd.to_datetime(df.Datetime, dayfirst=True)
#print(df.dtypes)
#print(df.Datetime.apply(lambda x : x.day_name()))
#print(df.Datetime.apply(lambda x : x.month_name()))
df = pd.read_csv('time_series_2.csv')
#print(df.head())
#print(df.dtypes)
df.Datetime = pd.to_datetime(df.Datetime, dayfirst=True)
print(df.head())
#print(df.dtypes)
df['Month'] = df.Datetime.dt.month
df['Month_name'] = df.Datetime.dt.month_name()
df['Day'] = df.Datetime.dt.day
df['Day_name'] = df.Datetime.dt.day_name()
df['Year'] = df.Datetime.dt.year
df['Today'] = pd.to_datetime(datetime.date.today())
diff_bet_dates = df['Today'] - df['Datetime']
#print(diff_bet_dates)
df['Day_difference'] = diff_bet_dates.apply(lambda x : x.days)
df['Asian_time'] = df.Datetime.dt.tz_localize('Asia/calcutta')
df['UTC_time']= df.Asian_time.dt.tz_convert('UTC')
print(df.head())