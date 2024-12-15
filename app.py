from flask import Flask, request, jsonify, redirect
from models import db, URL
from config import Config
from flask_cors import CORS
import random, string

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('original_url')
    if not original_url:
        return jsonify({'error': 'Original URL is required'}), 400

    short_url = generate_short_url()
    new_url = URL(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({'original_url': original_url, 'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    url_entry = URL.query.filter_by(short_url=short_url).first()
    if url_entry:
        return redirect(url_entry.original_url)
    return jsonify({'error': 'Short URL not found'}), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0",debug=True)

