import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# データの読み込み
df = pd.read_csv('ex3.csv')

print(f"先頭5行: {df.head(5)}\n")

# 6-3
# 回帰直線の式
# target = ax0 + bx1 + cx2 + dx3 + e

print("check error value...")
print(f"{df.isnull().any(axis = 0)}\n")
df2 = df.fillna(df.median())

# 散布図の描画
for col in df2.columns:
    if col == 'target':
        continue
    df2.plot.scatter(x = col, y = 'target')

# 外れ値の除去
no = df2[(df2['target'] > 100) & (df2['x2'] < -2)].index
df3 = df2.drop(no)

# 特徴量と正解データの分割
x = df3.loc[:, :'x3']
t = df3['target']

# 訓練データとテストデータに分割
x_train, x_test, t_train, t_test = train_test_split(x, t, test_size = 0.2, random_state = 1)

# 線形回帰モデルの準備
model = LinearRegression()

# モデルの学習
model.fit(x_train, t_train)

# モデルの評価
score = model.score(x_test, t_test)
print(f"決定係数: {score}\n")