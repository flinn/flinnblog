from flask import Flask, render_template, request, make_response, g
from flask.ext.wtf import Form, TextField, TextAreaField, HiddenField, ValidationError,\
                          Required, RecaptchaField
import models;

Models = models.BlogRepository()

class BlogController:	

	def Home(self):
		return render_template('index.html')

	def AllBlogs(self):
		allBlogs = Models.AllBlogs()
		return render_template('blogs.html', blogs=allBlogs)
    	
	def Contact(self):
		return render_template('contact.html', form=None)

	def About(self):
		aboutMe = "Text about me...Needs to be written."
		return render_template('about.html', aboutText=aboutMe)

	def Blog(self, id):
		blog = Models.GetBlog(blogId)
		return render_template('blog.html', blog=blog)