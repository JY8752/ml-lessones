import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# データの読み込み
df = pd.read_csv('Boston.csv')
print(df.head(2))