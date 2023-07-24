import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

# データの読み込み
df = pd.read_csv('Bank.csv')

# 特徴量と正解データに分割
# xcol = ['age', 'job', 'marital', 'education', 'default', 'amount', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous']
x = df.loc[:, 'age':'previous'].columns
t = df['y']

# 欠損値を確認する
print(df.isnull().sum())

# 訓練・検証データとテストデータに分割
train, test = train_test_split(df, test_size = 0.2, random_state = 0)

