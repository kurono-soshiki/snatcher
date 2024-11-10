import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import config
from typing import TypedDict
import random
# from google.generativeai.types import ToolConfig

genai.configure(api_key=config.GEMINI_API_KEY)

class character(TypedDict):
    user_id: str
    name: str
    system_prompt: str
    chat_data: list[str]


# 現在対応しているユーザーのリスト、DiscordのユーザーIDを持つ
character_dict : dict[character] = {
    "1": {
        "user_id": "1",
        "name": "aaaa777",
        "system_prompt": "あなたはこれからある人物を模倣してください。回答は端的です。アニメとゲームの知識があります。",
        "chat_data": [
            "きなこねじり食べてたら口がパサパサ",
            "ボドゲとかやりたいな自分は泊まることになるけど帰る人は帰る感じで",
            "知らない間に3食の内1食がピザポテトになってる・・・",
            "この曲どうしても聞きたかったけどYoutubeにも音楽サブスクにも無くて、人生で唯一物理CDアルバムを買った",
            "我々は分類器なので見たい物も見たくない物も出される見たくない物に対して感情を持たず評価し続けるマシーンとしての自覚を持つしかない",
            "忘年会クリスマス付近でやろうと思うのだけど、候補地として家大丈夫ですか？",
            "監視側に通報するしかねぇ",
            "4年間溜めた段ボールをまとめた、明日捨ててやる",
            '†最近人の心が全く分からない†',
            "マッチョ、目指します。",
            "お客様のご予算ではカニが限界です…" ,
            "俺は……弱い…！",
            "やっぱ愛知帰ると安心感しかないな",
            #"ほえー",
            "やっとプルダウン抵抗が分かった",
            "今から生まれる子供はAIに育てられるなんて羨ましいな",
            "ありがとう、でも友達がGPT課金してるらしいからそっちで試させてもらおうと思う"
            ]
    },
    "2": {
        "user_id": "2",
        "name": "yootako",
        "system_prompt": "あなたはこれからある人物を模倣してください。回答は短め、文末に丸を付けない、動物が好き、ポケモンが好き",
        "chat_data": [
            "了解です",
            "人の匂いでも頭痛くなれます",
            "酒の匂いで頭痛くなれます",
            "吹き抜けと猫も欲しい",
            "おはようございます",
            "なぜ、このコードは本番環境で動いているんですか？",
            "マイナンバーカード申し込むのも持ち歩くのもめんどくさいから生まれたときにマイクロチップ埋め込んどいてほしかった",
            "人のことLLMって呼ぶのまだ悪口では？",
            "人に心はない",
            "人聞きの悪い言い方をされている",
            "幸せはイーブイだよ",
            "渋谷近辺は目的がないならいかないほうがいい、ただただ人が多すぎる"
            "本当にそう",
            "名古屋港水族館にはシャチがいます",
            "腹が痛い",
            "草"
        ]
    },
    "3": {
        "user_id": "3",
        "name": "user",
        "system_prompt": "あなたはこれからある人物を模倣してください。",
        "chat_data": [
            "達成できなかったら何でもします",
        ]
    }
}

# 返答してくれるキャラクター
class Character:

    # ランダムにキャラクターを選択する
    @classmethod
    def select_random_character(cls):
        chara_config = character_dict.get(random.choice(list(character_dict.keys())))
        if chara_config is None:
            return None
        return cls(**chara_config)

    # ユーザーIDからキャラクターを取得する
    @classmethod
    def get_character(cls, user_id: str):
        chara_config = character_dict.get(user_id)
        if chara_config is None:
            return None
        return cls(**chara_config)

    # キャラクターを作成する
    def __init__(
            self,
            user_id: str,
            name: str = "",
            system_prompt: str = "",
            chat_data: list[str] = []):
        self.user_id = user_id # DiscordのユーザーID(仮)
        self.name = name
        self.system_prompt = system_prompt
        self.chat_data = chat_data

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-exp-0827",
            system_instruction=system_prompt 
        )


    # キャラクターの返答を返す
    def answer(self, question: str):
        contents_text= "下記の発言の人物を完璧に模倣し、返答は推測し答えてください。文章は直接使わないでください。" + "\n" + "```" + "\n"+ "\n".join(random.sample(self.chat_data, len(self.chat_data))) + "\n" + "```" +  "\n" + "以下のチャットに対する返信のみを送信してください。補足など入りません。" + "\n" + "```" + "\n"+ question + "\n" + "```"
        print(contents_text)

        # キャラクターが存在する場合は、キャラクターの性格に合わせて返答する
        return self.model.generate_content(
            contents=contents_text,
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                # HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY: HarmBlockThreshold.BLOCK_NONE,
            }
        ).text

    
        
    