from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/about')
def about():
    name = requests.get('https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png')
    try:
        return send_from_directory(name, path='/', as_attachment=True)
    except FileNotFoundError:
        abort(404)
    return name

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
