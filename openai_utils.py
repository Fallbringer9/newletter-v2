import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_weekly_news():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant qui résume les actus tech et cloud de la semaine."},
                {"role": "user", "content": "Peux-tu me donner un résumé court des 5 actus tech et cloud les plus importantes de cette semaine ?"}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Erreur lors de l'appel à l'API OpenAI :", e)
        return None

