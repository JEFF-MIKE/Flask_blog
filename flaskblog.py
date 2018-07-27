from flask import Flask, render_template
app = Flask(__name__)

# sample database call info
posts = [
    {
        'Author': "Michael Jefferies",
        "title": "Blog Post 1",
        "content: First post content",
        "date_posted": "April 21,2018"
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts="posts")

@app.route("/about")
def about():
    return "<h1>About Page</h1>"
