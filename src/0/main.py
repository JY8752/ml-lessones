from typing import List

# 1-1
# 標準入力で身長と体重を受け取り、BMIを計算する関数

def calc_bmi() -> float:
    height = float(input("身長を入力してください(m): "))
    weight = float(input("体重を入力してください(kg): "))
    return weight / height ** 2

print("BMIは{:f}です。".format(calc_bmi()))

# 2-2

def sum_score() -> None:
    scores: List[int] = []

    japanese = int(input("国語の点数を入力してください: "))
    scores.append(japanese)

    math = int(input("数学の点数を入力してください: "))
    scores.append(math)

    english = int(input("英語の点数を入力してください: "))
    scores.append(english)

    print("Japanese: {}, Math: {}, English: {}".format(japanese, math, english))
    print("合計点は{}点です。".format(sum(scores)))

sum_score()