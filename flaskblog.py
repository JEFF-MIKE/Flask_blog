from flask import Flask, render_template
app = Flask(__name__)

# sample database call info
posts = [
    {
        "author": "Michael Jefferies",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 21,2018"
    },
    {
        "author": "Some Random Guy",
        "title": "lol who's gonna look at this anyway",
        "content": "Second post content",
        "date_posted": "July 27,2018"
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")
