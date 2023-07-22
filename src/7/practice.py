import pandas as pd

# データの読み込み
df = pd.read_csv('ex4.csv')

print(f"先頭3行:\n {df.head(3)}\n")
      
# row_count = df.shape[0]
# male_count = df[df['sex'] == 0].shape[0]
mean = df['sex'].mean()
print(f"男性比率: {mean}%\n")

# classごとのscoreの平均値を求める
df2 = df.groupby('class').mean()['score']
print(f"各クラスの平均値:\n{df2}\n")

# class, sexごとのscoreの平均値を求める
pt = df.pivot_table(index = 'class', columns = 'sex', values = 'score', aggfunc = 'mean')
print(f"クラスと性別ごとの平均値:\n{pt}\n")

# dept_id列をダミー変数化
dummy_column = pd.get_dummies(df['dept_id'], drop_first = True)
df3 = pd.concat([df, dummy_column], axis = 1)
df3 = df3.drop('dept_id', axis = 1)
print(df3)