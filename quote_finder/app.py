from flask import Flask, render_template, request, redirect, url_for, flash
import json
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for flash messages

QUOTES_FILE = 'quotes.json'

def load_quotes():
    if not os.path.exists(QUOTES_FILE):
        return []

    with open(QUOTES_FILE, 'rb') as f:
        raw_bytes = f.read()
    print(f"Read {len(raw_bytes)} bytes from {QUOTES_FILE}")

    encodings_to_try = ['utf-8', 'utf-16', 'latin1']
    for enc in encodings_to_try:
        try:
            print(f"Trying to decode as {enc}")
            text = raw_bytes.decode(enc)
            quotes = json.loads(text)
            print(f"Successfully decoded and parsed JSON with {enc}")
            return quotes
        except UnicodeDecodeError as ude:
            print(f"UnicodeDecodeError decoding with {enc}: {ude}")
        except json.JSONDecodeError as jde:
            print(f"JSONDecodeError parsing JSON with {enc}: {jde}")

    raise Exception(f"Could not decode or parse {QUOTES_FILE} with any encoding.")



def save_quotes(quotes):
    # Always save as UTF-8 to keep things consistent
    with open(QUOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    quotes = load_quotes()
    random_quote = random.choice(quotes) if quotes else None
    return render_template('index.html', random_quote=random_quote)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword', '').lower()
        quotes = load_quotes()
        matched = [q for q in quotes if
                   keyword in q['quote'].lower() or
                   keyword in q['author'].lower() or
                   keyword in q['topic'].lower()]
        return render_template('result.html', keyword=keyword, quotes=matched)
    return render_template('search.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        quote = request.form.get('quote', '').strip()
        author = request.form.get('author', '').strip()
        topic = request.form.get('topic', '').strip().lower()

        if not quote or not author or not topic:
            flash('All fields are required.', 'error')
            return redirect(url_for('submit'))

        quotes = load_quotes()
        quotes.append({'quote': quote, 'author': author, 'topic': topic})
        save_quotes(quotes)
        flash('Quote submitted successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
