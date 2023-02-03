from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager # manages what web pages that we can access and what we cannot 

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ['hiangfaihueagurntagtngxa']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .views import views
    from .auth import auth 

    # basically have no prefix 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # need to import the .models to make sure to define the classes before initialize the database
    from .models import User, Note

    with app.app_context():
        db.create_all()  

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # works similar as filter by in query  
    
    return app
