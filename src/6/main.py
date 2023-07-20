import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def main():
    # データの読み込み
    df = pd.read_csv('cinema.csv')
    # 欠損値を穴埋め
    df2 = df.fillna(df.mean())

    # 散布図の描画
    for name in df2.columns:
        if name == 'cinema_id' or name == 'sales':
            continue
        df2.plot.scatter(x = name, y = 'sales')
    
    # 外れ値の除去
    no = df2[(df2['SNS2'] > 1000) & (df2['sales'] < 8500)].index
    df3 = df2.drop(no, axis = 0)

    # 特徴量と正解データの取り出し
    x = df3.loc[:, 'SNS1':'original']
    t = df3['sales']

    # 訓練データとテストデータに分割
    x_train, x_test, t_train, t_test = train_test_split(x, t, test_size = 0.2, random_state = 0)

    # 線形回帰モデルの準備
    model = LinearRegression()

    # モデルの学習
    model.fit(x_train, t_train)

    # 予測
    new = [[150, 700, 300, 0]]
    model.predict(new)

    # モデルの評価
    prod = model.predict(x_test)
    score = mean_absolute_error(t_test, prod)

    print('MAE: {}'.format(score))





main()