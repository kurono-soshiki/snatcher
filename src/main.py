# This example requires the 'message_content' intent.

import discord
import random

import config
from character import Character

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # BOT自身のメッセージは無視
    if message.author == client.user:
        pass

    # テスト用コマンド
    elif message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    # テキスト生成AIテストコマンド
    elif message.content.startswith('!genai'):
        # テキスト生成AIのリクエストを送信
        response = Character().answer('こんにちは')
        # リクエストの結果を送信
        await message.channel.send(response)

    # ユーザーが発言したときの処理
    else:
        # ユーザーの発言を取得
        user_message = message.content

        # 確率で返信する
        # if random.randint(0, 100) > 30:
        #     return

        # メンバーの人格の情報を取得
        chara = Character.select_random_character()

        # テキスト生成AIのリクエストを送信
        response = chara.answer(user_message)

        # リクエストの結果を送信
        await message.channel.send(response)
        

client.run(config.DISCORD_TOKEN)
