from flask import Flask, render_template, request, redirect, url_for, flash
import json
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)   # needed for flash messages

QUOTES_FILE = 'quotes.json'

def load_quotes():
    if not os.path.exists(QUOTES_FILE):
        return []

    try:
        with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except UnicodeDecodeError:
        try:
            with open(QUOTES_FILE, 'r', encoding='utf-16') as f:
                return json.load(f)
        except UnicodeDecodeError:
            with open(QUOTES_FILE, 'r', encoding='latin1') as f:
                return json.load(f)


# def load_quotes():
#     if not os.path.exists(QUOTES_FILE):
#         return []

#     try:
#         with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
#             return json.load(f)
#     except UnicodeDecodeError:
#         # Try fallback encoding
#         with open(QUOTES_FILE, 'r', encoding='latin1') as f:
#             return json.load(f)

# def load_quotes():
#     if not os.path.exists(QUOTES_FILE):
#         return []
#     with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
#         return json.load(f)

def save_quotes(quotes):
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