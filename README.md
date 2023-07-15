# [スッキリわかる機械学習入門](https://sukkiri.jp/books/sukkiri_ml)の学習用リポジトリ

## 環境構築

anacondaイメージをベースにJupiter Labを起動するdockerコンテナを使う。

```
# build
docker image build -t python-work .

# run
docker run -it -p 8888:8888 --rm --name python-work-container -v `pwd`/src:/work python-work
```

