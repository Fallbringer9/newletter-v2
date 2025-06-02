from openai_utils import get_weekly_news
from html_generator import generate_html_from_news

def main():
    print("📥 Récupération de l’actualité…")
    news = get_weekly_news()

    if news:
        print("🧾 Génération du fichier HTML…")
        html_content = generate_html_from_news(news)

        with open("newsletter.html", "w", encoding="utf-8") as file:
            file.write(html_content)

        print("✅ HTML généré avec succès → newsletter.html")
    else:
        print("❌ Échec lors de la récupération de l’actualité")

if __name__ == "__main__":
    main()
