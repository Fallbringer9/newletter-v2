import boto3
import os
from openai_utils import get_weekly_news
from html_generator import generate_html_from_news
from datetime import datetime
from bs4 import BeautifulSoup

# Initialise SNS
sns = boto3.client("sns")

# Récupère le nom du topic SNS depuis les variables d’environnement
sns_topic_arn = os.getenv("SNS_TOPIC_ARN")


def strip_html_tags(html):
    """Supprime les balises HTML pour générer du texte brut"""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def lambda_handler(event=None, context=None):
    print("📥 Récupération de l’actualité…")
    news = get_weekly_news()

    if not news:
        print("❌ Aucune actu récupérée")
        return {"statusCode": 500, "body": "Erreur de génération d’actualité"}

    print("🧾 Génération du contenu HTML…")
    html_content = generate_html_from_news(news)

    print("📤 Publication via SNS…")
    try:
        subject = f"🗞️ Newsletter - Semaine du {datetime.today().strftime('%d/%m/%Y')}"
        plain_text_message = strip_html_tags(html_content)

        response = sns.publish(
            TopicArn=sns_topic_arn,
            Subject=subject,
            Message=plain_text_message
        )

        print("✅ Message SNS publié :", response)
        return {"statusCode": 200, "body": "Newsletter envoyée avec succès"}

    except Exception as e:
        print("❌ Erreur d’envoi SNS :", str(e))
        return {"statusCode": 500, "body": "Erreur d’envoi via SNS"}

