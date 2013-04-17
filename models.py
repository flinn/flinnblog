from flask import Flask, render_template, request, make_response, g
import sqlite3

DATABASE = 'simpledata.db'
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def ReadBlogsFromCursor(cursor):
        blogs = [dict(id=row[0], title=row[1], description=row[2], blog_text=row[3], created_on=row[4], published_on=row[5], is_published=row[6], up_votes=row[7], down_votes=row[8], keywords=row[9], is_featured=row[10]) for row in cursor.fetchall()]
        return blogs

class BlogRepository:
    pass    

    def GetFeaturedBlogs(self):
        g.db = connect_db()
        cur = g.db.execute('SELECT * FROM blogs WHERE is_featured = 1 ORDER BY published_on DESC')
        blogs = ReadBlogsFromCursor(cur)
        g.db.close()
        return blogs

    def GetBlog(self, blogId):

        g.db = connect_db()
        cur = g.db.execute('SELECT * FROM blogs WHERE id = ' + str(blogId))
        blog = ReadBlogsFromCursor(cur)
        g.db.close()
        return blog

    def AllBlogs(self):
        g.db = connect_db()
        cur = g.db.execute('SELECT * FROM blogs')
        blogs = ReadBlogsFromCursor(cur)
        g.db.close()
        return blogs

    

class Blog:
    pass