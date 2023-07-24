import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

# データの読み込み
df = pd.read_csv('Bank.csv')

# ダミー変数化

# 文字列の列を抜き出す
str_col_name = ['job','default','marital','education','housing','loan','contact','month']
str_df = df[str_col_name]
dummies = pd.get_dummies(str_df, drop_first = True)


# 欠損値を確認する
print(df.isnull().sum())

# 欠損値を中央値で埋める
df = df.fillna(df.median())

# 訓練・検証データとテストデータに分割
train_valid, test = train_test_split(df, test_size = 0.2, random_state = 0)

# 特徴量と正解データに分割
# xcol = ['age', 'job', 'marital', 'education', 'default', 'amount', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous']
x = df.loc[:, 'age':'previous']
t = df['y']

# 決定木モデルの準備
model = tree.DecisionTreeClassifier(random_state = 0)

# モデルの学習
x_train, x_val, t_train, t_val = train_test_split(x, t, test_size = 0.2, random_state = 0)
model.fit(x_train, t_train)

# モデルの評価
score = model.score(x_val, t_val)
print(f"正解率: {score}")