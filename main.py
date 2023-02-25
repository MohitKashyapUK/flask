from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/about')
def about():
    return 'This is a about page, for sample!'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
