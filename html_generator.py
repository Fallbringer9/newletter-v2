from datetime import datetime

def generate_html_from_news(news: str) -> str:
    # On formate la date en français
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    mois_fr = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]
    now = datetime.now()
    jour = jours_semaine[now.weekday()]
    date_formatted = f"{jour} {now.day} {mois_fr[now.month - 1]} {now.year}"

    formatted_news = news.replace("\n", "<br>")

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Newsletter du {date_formatted}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
        }}
        .date {{
            color: #7f8c8d;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🗞️ Newsletter de la semaine</h1>
        <p class="date">{date_formatted}</p>
        <p>{formatted_news}</p>
    </div>
</body>
</html>
"""
    return html_content




