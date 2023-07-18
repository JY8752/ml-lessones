import pandas as pd

# データの読み込み
df = pd.read_csv('iris.csv')
data = df.head(3)

print(data.to_string())