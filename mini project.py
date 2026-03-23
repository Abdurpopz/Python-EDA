import pandas as pd

df = pd.read_csv(r"C:\Users\abdur\OneDrive\Documents\Desktop\python\raw_data.csv")
print(df)

# used for knowing data(if there are large amount of data we can know using this)

df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()


df = df.sort_values(by="order_id")
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['city'] = df['city'].fillna("unknown")
df['delivery_time'] = df['delivery_time'].fillna(df['delivery_time'].median())
df['order_time'] = pd.to_datetime(df['order_time']) #here pd.to_datetime(it is function) converts the order_time(which is string) to integer
df['order_hour'] = df['order_time'].dt.hour
df['day'] = df['order_time'].dt.day_name()


def speed(x):
    if x <= 30:
        return "Fast"
    elif x <= 45:
        return "Medium"
    else:
        return "slow"
    

df['delivery_speed'] = df['delivery_time'].apply(speed)
df.isnull().sum()
print(df.head())
#df.insert(df.columns.get_loc('delivery_time') + 1,
#'delivery_speed',
#df['delivery_time'].apply(speed))
          


from sqlalchemy import create_engine
username="root",
password="root",
host="localhost",
port="3306",
database="swiggy_test"

engine=create_engine(f"mysql+pymysql://root:root@localhost:3306/swiggy_test")
table_name="orders"
df.to_sql(table_name,engine,if_exists='replace',index=False)