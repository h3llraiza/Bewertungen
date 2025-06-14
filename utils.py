import json
import os

DATA_FILE = 'bewertungen.json'

def save_review(email, landlord, rating, comment):
    review = {
        'by': email,
        'rating': int(rating),
        'comment': comment
    }

    # Datei laden oder neue Liste erstellen
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}

    # Bewertungen nach Vermieter gruppieren
    if landlord not in data:
        data[landlord] = []

    data[landlord].append(review)

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_reviews_for_landlord(landlord):
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get(landlord, [])

def verify_user(email, file):
    allowed_domains = ['gmail.com', 'web.de', 'posteo.de']
    return '@' in email
