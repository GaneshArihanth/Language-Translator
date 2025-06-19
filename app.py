from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

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
            "x-rapidapi-key": "b3f908e177mshc6e18f1ad07cbb6p183bdbjsne93bc24941dc",
            "x-rapidapi-host": "google-translate113.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            translated = response.json()
            print("API response:", translated)  # Debug
            translated_text = translated.get("trans", {}).get("text", "Translation failed.")
        except Exception as e:
            translated_text = f"Error: {str(e)}"

    return render_template("index.html", language_map=language_map, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
