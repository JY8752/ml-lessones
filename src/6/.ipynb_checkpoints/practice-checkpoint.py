import pandas as pd

# データの読み込み
df = pd.read_csv('ex3.csv')

print(f"先頭5行: {df.head(5)}")

# 6-3
# 回帰直線の式
# target = ax0 + bx1 + cx2 + dx3 + e

print(df.isnull().any(axis = 0))