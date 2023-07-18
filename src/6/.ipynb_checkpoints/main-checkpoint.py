import pandas as pd

def main():
    # データの読み込み
    df = pd.read_csv('cinema.csv')
    # 欠損値を穴埋め
    df2 = df.fillna(df.mean())

    # 散布図の描画
    %matplotlib inline
    for name in df2.columns:
        if name == 'cinema_id' or name == 'sales':
            continue
        df2.plot.scatter(kind = 'scatter', x = name, y = 'sales')

main()