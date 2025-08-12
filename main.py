import json
from flask import Flask, render_template

app = Flask(__name__)

# Load posts from JSON file
with open('posts.json', 'r') as f:
    blog_posts = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
