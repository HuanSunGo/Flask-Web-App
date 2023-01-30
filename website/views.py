from flask import Blueprint, render_template # a way to seperate my web app out

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # this function will run whenever go to the '/' root
    return render_template("home.html")
    

