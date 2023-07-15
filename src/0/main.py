from typing import List

# 1-1
# 標準入力で身長と体重を受け取り、BMIを計算する関数

def calc_bmi() -> float:
    height = float(input("身長を入力してください(m): "))
    weight = float(input("体重を入力してください(kg): "))
    return weight / height ** 2

# print("BMIは{:f}です。".format(calc_bmi()))

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

# sum_score()

# 3-1
# 偶数か奇数かを判定する関数

def even_or_odd() -> None:
    num = int(input("整数を入力してください: "))
    if num % 2 == 0:
        print("偶数です。")
    else:
        print("奇数です。")

# even_or_odd()

def hello() -> None:
    str = input("何か文字を入力してください: ")
    if str == "こんにちは":
        print("ようこそ!")
    elif str == "景気は？":
        print("ぼちぼちです。")
    elif str == "さようなら":
        print("お元気で!")
    else:
        print("どうしました？")

# hello()

# 4-1

def count_down() -> None:
    for i in range(10, 0, -1):
        print("{}, ".format(i), end="")
    print("Lift off!")

# count_down()

# 4-2

def calc_score() -> None:
    scores: List[int] = [71, 67, 73, 61, 79, 59, 83, 87, 72, 79]
    final_scores: List[int] = list(map(lambda score: score * 0.8 + 20, scores))
    average = sum(final_scores) / len(final_scores)
    print("平均点は{}点です。".format(average))

calc_score()

# 5-1
# うるう年かどうかを判定する関数

def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False
    
is_leap_year(2020)
