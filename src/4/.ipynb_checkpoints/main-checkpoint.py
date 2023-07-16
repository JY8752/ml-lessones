import pandas as pd
from sklearn import tree

# データの読み込み
df = pd.read_csv('KvsT.csv')

# 特徴量と正解データに分割
xcol = ['身長', '体重', '年齢']
x = df[xcol]
t = df['派閥']

# モデルの準備(決定木モデル)
model = tree.DecisionTreeClassifier(random_state = 0)

# モデルの学習
model.fit(x, t)

# モデルの評価
print(model.score(x, t))