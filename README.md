## Snatcher
Discordの発言を学習し、勝手に模倣して勝手に返事をするBot

# 起動方法
python3.12とpoetryが必要です
  
  ```
  poetry install
  poetry run python3.12 main.py
  ```

# CLI
Discordを介さずCharacterのみ起動する

```
poetry run python3 src/cli.py
```



# 仕様

## 発言条件
- 勝手に応答する

1. 特定のチャンネルで誰かが発言する
2. 勝手に返事をする(返事の確率30%とか)


- 発言は誰かを模倣する
- 模倣する相手はランダムでチャンネルにいる人を抽選

# 詳細設計

## 模倣する内容
- 設定したチャンネルの発言を収集して模倣する(generalを想定)
  - ハードコードなので手動でがんばれる

## 模倣するデータを収集するタイミング
- ハードコードする(あらかじめ用意する)