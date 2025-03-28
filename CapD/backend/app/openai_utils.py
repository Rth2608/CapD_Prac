import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str) -> str:
    try:
        prompt = f"다음 뉴스 내용을 한국어로 간단히 요약해줘:\n{text[:4000]}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"[OpenAI Error] {e}")
        return "요약 실패"
