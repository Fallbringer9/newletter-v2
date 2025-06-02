import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_weekly_news():
    try:
        print("📥 Récupération de l’actualité…")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant expert en technologie et cloud."},
                {"role": "user", "content": "Donne-moi un résumé concis, structuré et engageant des actualités tech, cloud, IA et dev de la semaine."}
            ],
            temperature=0.7
        )

        content = response["choices"][0]["message"]["content"]
        return content

    except Exception as e:
        print("❌ Erreur lors de l'appel à l'API OpenAI :", e)
        return None


