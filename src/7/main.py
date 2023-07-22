import pandas as pd
from pandas.core.frame import DataFrame
from sklearn import tree
from sklearn.model_selection import train_test_split
from typing import Tuple

def learn(x: DataFrame, t: DataFrame, depth: int = 3) -> Tuple[float, float, tree.DecisionTreeClassifier]:
    x_train, x_test, t_train, t_test = train_test_split(x, t, test_size = 0.2, random_state = 0)
    model = tree.DecisionTreeClassifier(random_state = 0, max_depth = depth, class_weight = 'balanced')
    model.fit(x, t)

    score = model.score(x_train, t_train)
    score2 = model.score(x_test, t_test)
    return score, score2, model

# データの読み込み
df = pd.read_csv('Survived.csv')

# 欠損値を中央値で埋める
# df = df.fillna(df.median())

# ピボットテーブルの作成
pt = pd.pivot_table(df, index = 'Survived', columns = 'Pclass', values = 'Age')
print(pt)

is_null = df['Age'].isnull()

# Pclass 1に関する埋め込み
df.loc[(df['Pclass'] == 1) & (df['Survived'] == 0) & (is_null), 'Age'] = 43
df.loc[(df['Pclass'] == 1) & (df['Survived'] == 1) & (is_null), 'Age'] = 35

# Pclass 2に関する埋め込み
df.loc[(df['Pclass'] == 2) & (df['Survived'] == 0) & (is_null), 'Age'] = 33
df.loc[(df['Pclass'] == 2) & (df['Survived'] == 1) & (is_null), 'Age'] = 25

# Pclass 3に関する埋め込み
df.loc[(df['Pclass'] == 3) & (df['Survived'] == 0) & (is_null), 'Age'] = 26
df.loc[(df['Pclass'] == 3) & (df['Survived'] == 1) & (is_null), 'Age'] = 20

# Sex列を数値に変換
male = pd.get_dummies(df['Sex'], drop_first = True)
print(male)

# 特徴量と正解データに分割
col = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex']
x = df[col]
t = df['Survived']

# male列を追加
x_temp = pd.concat([x, male], axis = 1)
x_new = x_temp.drop('Sex', axis = 1)

for i in range(1, 6):
    s1, s2, model = learn(x_new, t, i)
    print(f"depth: {i}, score: {s1}, score2: {s2}")
