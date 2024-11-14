# Snatcher
Discordの発言を学習し、勝手に模倣して勝手に返事をするBot

## 人格の設計について
Character内のインスタンス変数は人間の動きをシミュレーションするパラメータとなる

## 起動方法
python3.12とpoetryが必要です
  
  ```
  poetry install
  poetry run python3.12 main.py
  ```

## CLI
Discordを介さずCharacterのみ起動する

```
poetry run python3 src/cli.py
```


# 仕様

## 発言トリガー
発言を行うには以下の共通条件を満たした上でトリガーが発火される必要がある

- 指定のチャンネル内である

1. トリガー: 誰かの発言
返答する形でメッセージを送る

- 発言者がBotではない
- 確率抽選を突破する(30%)

2. トリガー: 定期実行
独り言のようにつぶやく

- 今日、定期実行で発言した回数が3回未満
- 9:00 ~ 23:00の中で30分毎に確率抽選(5%)

## 発言内容

- 発言は誰かを模倣する
- 模倣する相手はランダム

## 発言のもととなるデータ

- Discordのメッセージ

# モデリング・クラス設計
それぞれの人格はCharacterクラスを用いて操作する  
Characterには`キャラクターブック`が存在し、これが人格を司る  
Characterは現在の`状態(State)`を`注意(Attention)`として保存する  
プロンプトは`システムメッセージ`+`キャラクターブック`+`注意`によって構築される  

## Character
LLMを用いて作成した人格を扱うクラス

### 関数
- answer(question: str): str
- monologue(): str
- train_answer(question: str, answer: str): str
- train_monologue(): str


### インスタンス変数
- attention_prompt キャラクタの注意、体調・最近見たニュースによる話題・現在の思考を作る
- character_prompt キャラクターブック、強いキャラクターの印象を作る

### 一時的な設計
現在ハードコードによってキャラクターを作成しているが、最終的には設定したチャンネルから情報を自動収集するようになる

