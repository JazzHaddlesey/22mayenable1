
from flask import Flask, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite///:data.bd" #os.getenv("DATABASE_URI")

db = SQLAlchemy(app)


class customer(db.Model):
    id = db.column(db.Integer, primary_key=True)
    f_name = db.column(db.String,(30), nullable=False)
    l_name = db.column(db.String,(30), nullable=False)
    
db.create_all()

@app.route('/')
def home():
    return "<h1>Hello Internet!</h1>"

@app.route('/content')
def content():
    return "<h1>Goodbye Internet!</h1>\n<p>Government mind control methods.</p>\n<strong>Lizard People!</strong>"

@app.route('/diff', methods = ["GET", "POST"])
def get_post():
    if request.method == "POST":
      return "<h2>Post Request</h2>"
    else:
        return "<h2>Get Request</h2>"
    
@app.route("/redirects")
def redirects():
    return redirect("https://www.google.com")

@app.route("/edit/<word>")
def multiplier(word):
    return f"<h1>{word * 5}</h1>"

@app.route("/urlfor")
def urlfor():
    return redirect(url_for("home"))


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
