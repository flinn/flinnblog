import sqlite3 as lite
import sys

blogsList = (
    (1, 'Looking Forward'),
    (2, 'Write SOLID Code.'),
    (3, 'What Stops You?')
)

con = lite.connect('whoisflinn.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS blogs")
    cur.execute("CREATE TABLE blogs(id INT, title TEXT)")
    cur.executemany("INSERT INTO blogs VALUES(?, ?)", blogsList)