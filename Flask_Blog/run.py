# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:23:38 2020

@author: Ulka Khobragade
"""
#Grab and run the app Only function of this file
from flaskblog import create_app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
