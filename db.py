import sqlite3 as lite
import sys
import os

blogDesc1 = '<p>I set quite a few goals for myself this year. Amongst them, the creation of this blog. While this site is still <i>very</i> much a work in progress, I\'m excited to have produced something tangible.</p><p>I set quite a few goals for myself this year. Amongst them, the creation of this blog. While this site is still <i>very</i> much a work in progress, I\'m excited to have produced something tangible.</p>'
blogDesc2 = '<p>I\'m teaching a class on the basic principles of <span class="highlighter">Object-Oriented Software Design</span> to new developers starting work at The Motley Fool. The main focus of the class will be on writing SOLID code. What\'s that? Let me explain.</p><p><span class="thought">(<i>Also, I figured this would provide as good an opportunity as any for me to test out the presentation framework called impress.js</i>)</span> </p>'
blogDesc3 = '<p>So you took your friend\'s advice <span class="thought">(<i>and perhaps that friend was me?</i>)</span>, or maybe you were just genuinely interested, and you finally learned how to program.</p><p>You know how to write code. But what now? <span class="highlighter">"How do I make a website using all these \'if\' statements and \'for\' loops?"</span>, you ask. Let me help you get started.</p>'

blogText = 'Fake blog text goes here.'

blogsList = (
    (1, 'Looking Forward', blogDesc1, blogText, '3/20/2013', '4/11/2013', True, 3, 0, 'Life', True),
    (2, 'Write SOLID Code.', blogDesc2, blogText, '3/22/2013', '5/12/2013', False, 0, 0, 'Code', True),
    (3, 'What Stops You?', blogDesc3, blogText, '3/10/2013', '4/5/2013', True, 4, 1, 'Inspiration', True),
)

con = lite.connect('simpledata.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS blogs")
    cur.execute("CREATE TABLE blogs(id INT, title TEXT, description TEXT, blog_text TEXT, created_on DATE, published_on DATE, is_published BOOLEAN, up_votes INT, down_votes INT, keywords TEXT, is_featured BOOLEAN)")
    cur.executemany("INSERT INTO blogs VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", blogsList)