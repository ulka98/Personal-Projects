# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:49:26 2020

@author: Ulka Khobragade
"""

from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#in functions below an html code can be retured
#inside triple quotes '''  code ''' which is ugly. So we Use Templates
#some dummy data in post
# TO protect from any attack and outside changes, etc.
#import secrets-->secrets.token_hex(16)--->16 is the no of bytes
app.config['SECRET_KEY'] = 'f19e276a90593ef547fb1d6e9bb964ce'

posts = [
        {
            'author':'Ulka Khobragade',
            'title' :'Blog Post 1',
            'content' :'First post content',
            'date_posted': 'June 21, 2020'
                },
        {
            'author':'Rakshita Khobragade',
            'title' :'Blog Post 2',
            'content' :'Second post content',
            'date_posted': 'June 27, 2020'
                }

        ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('main.home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == 'password':
            flash("You have been logged in!",'success')
            return redirect(url_for('main.home'))
        else:
            flash("Log in Unsuccessful. Please check username and password",'danger')
    return render_template('login.html',title='Login',form=form)



if __name__ == "__main__":
    app.run(debug=True)
