#!/usr/bin/env python
# coding=utf8
import os
from flask import Flask, render_template, request, make_response, g
from functools import wraps
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form, TextField, TextAreaField, HiddenField, ValidationError,\
                          Required, RecaptchaField
import sqlite3
import models;
import controllers;

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = False
app.config['BOOTSTRAP_USE_CDN'] = False
app.config['BOOTSTRAP_FONTAWESOME'] = False
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

Controller = controllers.BlogController()  

@app.route('/', methods=('GET', 'POST',))
def index():
    return Controller.Home()    

@app.route('/about', methods=('GET', 'POST',))
def about():
    return Controller.About()

@app.route('/contact', methods=('GET', 'POST',))
def contact():
    return Controller.Contact()        

@app.route('/blog/create', methods=('GET', 'POST',))
def createblog(): 
    return Controller.CreateBlog()

@app.route('/blog/all', methods=('GET', 'POST'))
def allbogs():
    return Controller.AllBlogs()

@app.route('/blog/<int:blogId>', methods=('GET', 'POST'))
def blog(blogId):
    if blogId != 0:
        return Contoller.Blog(blogId)
    
    return Controller.AllBlogs()
    

if '__main__' == __name__:
    app.run(debug=True)
