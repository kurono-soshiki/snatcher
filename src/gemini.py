# geminiのAPIのテスト用コード

import google.generativeai as genai
import os
import config

genai.configure(api_key=config.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)


