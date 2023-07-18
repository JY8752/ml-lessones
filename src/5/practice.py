import pandas as pd
from pandas.core.frame import DataFrame
from sklearn import tree
from sklearn.model_selection import train_test_split

def new_dataframe_filled_median(df: DataFrame, column_name: str) -> DataFrame:
    col_median = df[column_name].median()
    return df[column_name].fillna(col_median)

# データの読み込み
df = pd.read_csv('ex2.csv')
print(f"学習データの先頭3件: \n{df.head(3)}\n")

print(f"データフレームの行数と列数: {df.shape}\n")

print(f"target列のデータの数: \n{df['target'].value_counts()}\n")

print(f"x0列の欠損値の数: {df['x0'].isnull().sum()}")
print(f"x1列の欠損値の数: {df['x1'].isnull().sum()}")
print(f"x2列の欠損値の数: {df['x2'].isnull().sum()}")
print(f"x3列の欠損値の数: {df['x3'].isnull().sum()}")
print(f"target列の欠損値の数: {df['target'].isnull().sum()}\n")

df2 = df.fillna(df.median())

# if df['x0'].isnull:
#     df['x0'] = new_dataframe_filled_mean(df, 'x0')

# if df['x1'].isnull:
#     df['x1'] = new_dataframe_filled_mean(df, 'x1')

# if df['x2'].isnull:
#     df['x2'] = new_dataframe_filled_mean(df, 'x2')

# if df['x3'].isnull:
#     df['x3'] = new_dataframe_filled_mean(df, 'x3')

# if df['target'].isnull:
#     df['target'] = new_dataframe_filled_mean(df, 'target')

# print(f"欠損値を中央値で埋めた後のデータフレーム: \n{df.isnull().any(axis = 0)}")

xcol = ['x0', 'x1', 'x2', 'x3']
x = df2[xcol]

t = df2['target']

model = tree.DecisionTreeClassifier(random_state = 0, max_depth = 3)

x_train, x_test, t_train, t_test = train_test_split(x, t, test_size = 0.2, random_state = 0)

model.fit(x_train, t_train)
score = model.score(x_test, t_test)

print(f"正解率: {score}")

infer = model.predict([[1.56, 0.23, -1.1, -2.8]])
print(f"推論結果: {infer}")