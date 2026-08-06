from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOG_API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

def get_all_posts():
    response = requests.get(BLOG_API_URL)
    return response.json()

@app.route('/')
def home():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    posts = get_all_posts()
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)