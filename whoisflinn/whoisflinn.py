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

DATABASE = 'whoisflinn.db'

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = False
app.config['BOOTSTRAP_USE_CDN'] = False
app.config['BOOTSTRAP_FONTAWESOME'] = False
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


class ContactForm(Form):
    name = TextField('Name', default="Your Name", validators=[Required()])
    email = TextField('Email', default="Your Email", validators=[Required()])
    message = TextAreaField(u'Message', default="Your Message")
    hidden_field = HiddenField('You cannot see this', description='Nope')
    recaptcha = RecaptchaField('Prove Your Humanity')
    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')       

@app.route('/', methods=('GET', 'POST',))
def index():    
    return render_template('index.html')

@app.route('/about', methods=('GET', 'POST',))
def about():
    isDev = False
    isKnown = False

    if request.cookies.get('dev') != None:
        isDev = request.cookies.get('dev') == 'True'
        isKnown = True

    if isKnown == False and request.args.get('dev') != None:
        isDev = request.args.get('dev') == 'True'
        isKnown = True        
    
    if isDev:
        aboutMe = "Welcome to the cool club, bro!"        
    else:
        aboutMe = "You're not a developer. You shithead."        

    resp = make_response(render_template('about.html', aboutText=aboutMe, known=isKnown))
    resp.set_cookie('dev', value=isDev)
    return resp

@app.route('/contact', methods=('GET', 'POST',))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return "PASSED"
    return render_template('contact.html', form=form)

@app.route('/blog/all', methods=('GET', 'POST'))
def blogs():
    g.db = connect_db()
    cur = g.db.execute('SELECT * FROM blogs')
    blogs = [dict(id=row[0], title=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('blogs.html', blogs=blogs)

@app.route('/blog/<int:blogId>', methods=('GET', 'POST'))
def blog(blogId):    
    blog = None    
    repository = models.BlogRepository()
    if blogId != 0:
        blog = repository.GetBlog(blogId)
    else: 
        return redirect(url_for('/blog/all'))

    return render_template('blog.html', blog=blog)

if '__main__' == __name__:
    app.run(debug=True)
