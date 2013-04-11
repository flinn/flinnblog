from flask import Flask, render_template, request, make_response, g
import sqlite3

DATABASE = 'whoisflinn.db'
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

class BlogRepository:
    pass    

    def GetBlog(self, blogId):
        exampleBlog1 = Blog()
        exaR0ckkrush3r885
        mpleBlog1.title = 'Example Blog #1'
        exampleBlog1.text = 'This is the example blog #1 text.'
        exampleBlog1.description = ''
        exampleBlog1.id = 10

        exampleBlog2 = Blog()
        exampleBlog2.title = 'Totally Different #2'
        exampleBlog2.text = 'The quick brown blog#2 fox jumped <i>over</i> the lazy log.'
        exampleBlog2.description = ''
        exampleBlog2.id = 11

        if blogId == 1:
            return exampleBlog1
        if blogId == 2:
            return exampleBlog2

    def AllBlogs(self):
        g.db = connect_db()
        cur = g.db.execute('SELECT * FROM blogs')
        blogs = [dict(id=row[0], title=row[1]) for row in cur.fetchall()]
        g.db.close()
        return blogs

class Blog:
    pass