# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:23:34 2020

@author: Ulka Khobragade
"""

from flask import Flask, render_template,url_for

app = Flask(__name__)

#in functions below an html code can be retured 
#inside triple quotes '''  code ''' which is ugly. So we Use Templates
#some dummy data in post

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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')




if __name__ == "__main__":
    app.run(debug=True)