import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_posts():
    with open('posts.json', 'r') as f:
        return json.load(f)

def save_posts(posts):
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=4)

def fetch_post_by_id(post_id):
    posts = get_posts()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = get_posts()
        max_id = max(post['id'] for post in posts) if posts else 0
        new_post = {
            "id": max_id + 1,
            "author": request.form.get('author'),
            "title": request.form.get('title'),
            "content": request.form.get('content')
        }
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = get_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404
    
    if request.method == 'POST':
        posts = get_posts()
        for p in posts:
            if p['id'] == post_id:
                p['title'] = request.form['title']
                p['author'] = request.form['author']
                p['content'] = request.form['content']
                break
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
