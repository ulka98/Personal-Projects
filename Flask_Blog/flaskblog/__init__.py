# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:42:06 2020

@author: Ulka Khobragade
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

#in functions below an html code can be retured
#inside triple quotes '''  code ''' which is ugly. So we Use Templates
#some dummy data in post
# TO protect from any attack and outside changes, etc.
#import secrets-->secrets.token_hex(16)--->16 is the no of bytes

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' #same thing as url_for() for decorater to know the location of login route
login_manager.login_message_category = 'info' #info the bootstrap class is the blue coloerd information for better css flashed message
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
