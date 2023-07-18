import pandas as pd
from sklearn import tree, train_test_split
import pickle

# データの読み込み
df = pd.read_csv('iris.csv')

# 各列の中央値を計算
col_mean = df.mean()

# 欠損値を中央値で埋める
df2 = df.fillna(col_mean)

# 特徴量と正解データに分割
xcol = ['がく片長さ', 'がく片幅', '花弁長さ', '花弁幅']
x = df2[xcol]
t = df2['種類']

# 訓練データとテストデータに分割
x_train, x_test, t_train, t_test = train_test_split(x, t, test_size = 0.3, random_state = 0)

# 決定木モデルの準備
tree_model = tree.DecisionTreeClassifier(random_state = 0)

tree_model.fit(x_train, t_train)
score = tree_model.score(x_test, t_test)

print('正解率: {}'.format(score))

# モデルの保存
with open('irismodel.pkl', mode = 'wb') as fp:
    pickle.dump(tree_model, fp)