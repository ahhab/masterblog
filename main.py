import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
