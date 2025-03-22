# X Searcher

twikitにより下記を行うCLIツール
- 指定アカウントのツイート最新300件を取得
- 平均インプレッション数を計算
- 平均以上のツイートを抽出・表示

twitter apiの無料枠は制限が強いためtwikitというライブラリによってスクレイピングすることで情報を疑似API的に取得している。

https://github.com/user-attachments/assets/098801dc-6198-41d6-a0aa-4ae9f9d35f91

## Usage

1. pythonとpoetryをインストール
2. Xの捨てアカを作成
3. 下記を実行

```
$ cp example.env .env
# => 取得に利用するアカウント情報を入力
$ poetry run python main.py
# => 取得対象のユーザーIDを入力
```
