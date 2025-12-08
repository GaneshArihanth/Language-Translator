from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

language_map = {
    1: ('English', 'en'), 2: ('French', 'fr'), 3: ('Spanish', 'es'),
    4: ('German', 'de'), 5: ('Italian', 'it'), 6: ('Portuguese', 'pt'),
    7: ('Russian', 'ru'), 8: ('Chinese (Simplified)', 'zh'),
    9: ('Japanese', 'ja'), 10: ('Korean', 'ko'), 11: ('Hindi', 'hi'),
    12: ('Tamil', 'ta'), 13: ('Telugu', 'te'), 14: ('Bengali', 'bn'),
    15: ('Gujarati', 'gu'), 16: ('Kannada', 'kn'), 17: ('Malayalam', 'ml'),
    18: ('Marathi', 'mr'), 19: ('Punjabi', 'pa'), 20: ('Urdu', 'ur'),
    21: ('Arabic', 'ar'), 22: ('Turkish', 'tr'), 23: ('Vietnamese', 'vi'),
    24: ('Thai', 'th'), 25: ('Dutch', 'nl'), 26: ('Greek', 'el'),
    27: ('Hebrew', 'iw'), 28: ('Polish', 'pl'), 29: ('Ukrainian', 'uk'),
    30: ('Romanian', 'ro')
}

@app.route('/', methods=['GET', 'POST'])
def index():
    # Keep existing route for backward compatibility or simple testing
    translated_text = ''
    if request.method == 'POST':
        text_to_translate = request.form['text']
        language_code = request.form['language']
        
        url = "https://google-translate113.p.rapidapi.com/api/v1/translator/json"
        payload = {
            "from": "auto",
            "to": language_code,
            "json": {
                "text": text_to_translate
            }
        }

        headers = {
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
            "x-rapidapi-host": "google-translate113.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            translated = response.json()
            translated_text = translated.get("trans", {}).get("text", "Translation failed.")
        except Exception as e:
            translated_text = f"Error: {str(e)}"

    return render_template("index.html", language_map=language_map, translated_text=translated_text)

@app.route('/api/languages', methods=['GET'])
def get_languages():
    # Convert dictionary to a list of objects for easier frontend consumption
    languages = [{"id": k, "name": v[0], "code": v[1]} for k, v in language_map.items()]
    return jsonify(languages)

@app.route('/api/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_to_translate = data.get('text')
    language_code = data.get('target_lang')

    if not text_to_translate or not language_code:
        return jsonify({"error": "Missing text or target_lang"}), 400

    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/json"
    payload = {
        "from": "auto",
        "to": language_code,
        "json": {
            "text": text_to_translate
        }
    }

    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": "google-translate113.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        translated = response.json()
        translated_text = translated.get("trans", {}).get("text", "Translation failed.")
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
