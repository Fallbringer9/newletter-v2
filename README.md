#  Newsletter V2

Ce projet génère automatiquement une newsletter hebdomadaire à l'aide de l'API d'OpenAI, la formate en HTML, puis l'envoie par e-mail via **Amazon SNS**. Le tout est automatisé grâce à **AWS Lambda** et **EventBridge Scheduler**.

##  Stack Technique

- **Python 3.11**
- **OpenAI API** (génération de contenu)
- **BeautifulSoup** (conversion HTML → texte)
- **boto3** (interactions AWS)
- **AWS Lambda** (exécution serverless)
- **Amazon SNS** (envoi d’e-mails)
- **AWS EventBridge** (planification automatique chaque lundi)
- **GitHub** (versioning)

## Fonctionnement

1. Un événement **EventBridge** déclenche la fonction Lambda chaque **lundi à 19h03 (Europe/Paris)**.
2. Lambda utilise l’API **OpenAI** pour générer l’actu tech de la semaine.
3. Le texte est converti en HTML avec `generate_html_from_news`.
4. Le HTML est transformé en texte brut avec `BeautifulSoup`.
5. Le message est publié sur un **topic SNS**, qui envoie l’e-mail.

## Sécurité

- La clé OpenAI est stockée dans un `.env` (non versionné).
- L’accès SNS est autorisé via une **policy IAM dédiée**.
- L’invocation Lambda via EventBridge est restreinte par une **resource-based policy**.



