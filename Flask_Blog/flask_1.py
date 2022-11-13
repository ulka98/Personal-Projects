# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:32:39 2020

@author: Ulka Khobragade
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"




if __name__ == "__main__":
    app.run(debug=True)