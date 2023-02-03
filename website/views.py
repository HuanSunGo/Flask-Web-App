from flask import Blueprint, render_template # a way to seperate my web app out
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # this function will run whenever go to the '/' root
    return render_template("home.html", user = current_user)
    

