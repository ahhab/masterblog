import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_posts():
    with open('posts.json', 'r') as f:
        return json.load(f)

def save_posts(posts):
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=4)

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = get_posts()
        new_post = {
            "id": len(posts) + 1,
            "author": request.form.get('author'),
            "title": request.form.get('title'),
            "content": request.form.get('content')
        }
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
