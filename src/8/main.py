import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from typing import Tuple

def getScaler(df: pd.DataFrame) -> pd.DataFrame:
    scaler = StandardScaler()
    scaler.fit(df)
    return scaler

def learn(x: DataFrame, t: DataFrame) -> Tuple[float, float, StandardScaler, StandardScaler, LinearRegression]:
    x_train, x_val, t_train, t_val = train_test_split(x, t, test_size = 0.2, random_state = 0)

    sc_x = getScaler(x_train)
    sc_t = getScaler(t_train)

    # 訓練データを標準化
    sc_x_train = sc_x.transform(x_train)
    sc_t_train = sc_t.transform(t_train)

    # モデルの学習
    model = LinearRegression()
    model.fit(sc_x_train, sc_t_train)

    # 検証データの標準化
    sc_x_val = sc_x.transform(x_val)
    sc_t_val = sc_t.transform(t_val)

    # 決定係数の計算
    x_score = model.score(sc_x_val, sc_t_val)
    t_score = model.score(sc_x_train, sc_t_train)

    return x_score, t_score, sc_x, sc_t, model

# データの読み込み
df = pd.read_csv('Boston.csv')
print(df.head(2))

# CRIME列をダミー値に変換
crime = pd.get_dummies(df['CRIME'], drop_first = True)
df = pd.concat([df, crime], axis = 1)
df = df.drop('CRIME', axis = 1)

print(f"{df.head(2)}\n")

# 欠損値の処理
train_val, test = train_test_split(df, test_size = 0.2, random_state = 0)

# 欠損値の確認
print(f"欠損値の確認: \n{train_val.isnull().sum()}\n")

train_val = train_val.fillna(train_val.mean())

# 外れ値を除去するために散布図を描画
# for col in train_val.columns:
#     train_val.plot.scatter(x = col, y = 'PRICE')

# 特徴量にはindus, nox, rm, piration, lstatを使用する

# 外れ値の除去
rm_out_val = train_val[(train_val['RM'] < 6) & (train_val['PRICE'] > 40)].index
ptration_out_val = train_val[(train_val['PTRATIO'] > 18) & (train_val['PRICE'] > 40)].index

print(f"rm_out_val: {rm_out_val}\n")
print(f"ptration_out_val: {ptration_out_val}\n")

# 両方外れ値のインデックスは76なので
train_val = train_val.drop([76], axis = 0)

# 使用する列だけに絞り込む
train_val = train_val[['INDUS', 'NOX', 'RM', 'PTRATIO', 'LSTAT', 'PRICE']]
print(f"先頭3行: \n{train_val.head(3)}\n")

# 相関係数を確認
print(f"相関係数: \n{train_val.corr()['PRICE'].map(abs).sort_values(ascending = False)}\n")

# 相関関係が強いrm, lstat, ptrationの3つを特徴量として使用する
x: DataFrame = train_val[['RM', 'PTRATIO', 'LSTAT']]
t: DataFrame = train_val[['PRICE']]

# 2乗項を追加
x['RM2'] = x['RM'] ** 2
x['PTRATIO2'] = x['PTRATIO'] ** 2
x['LSTAT2'] = x['LSTAT'] ** 2

# 交互作用項を追加
x['RM_LSTAT'] = x['RM'] * x['LSTAT']

x_score, t_score, sc_x, sc_t, model = learn(x, t)

print(f"決定係数(訓練データ): {x_score}\n")
print(f"決定係数(検証データ): {t_score}\n")

# テストデータの前処理
test = test.fillna(test.mean())

x_test = test[['RM', 'PTRATIO', 'LSTAT']]
t_test = test[['PRICE']]

# 2乗項を追加
x_test['RM2'] = x_test['RM'] ** 2
x_test['PTRATIO2'] = x_test['PTRATIO'] ** 2
x_test['LSTAT2'] = x_test['LSTAT'] ** 2

# 交互作用項を追加
x_test['RM_LSTAT'] = x_test['RM'] * x_test['LSTAT']

# テストデータを標準化
sc_x_test = sc_x.transform(x_test)
sc_t_test = sc_t.transform(t_test)

# 決定係数の計算
print(f"決定係数(テストデータ): {model.score(sc_x_test, sc_t_test)}\n")