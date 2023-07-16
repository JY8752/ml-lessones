import pandas as pd
from typing import Dict, List

# データの読み込み
data: Dict[str, List[int]] = {
    'データベースの試験得点', [70, 72, 75, 80],
    'ネットワークの試験得点', [80, 85, 79, 92]
}

df = pd.DataFrame(data)

# インデックスのへんこう
df.index = ['一郎', '次郎', '三郎', '太郎']

print(df.to_string())