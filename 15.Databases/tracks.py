#Multi-Table Database - Tracks
import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
''')

fname = input('Enter file name (.xml): ')

try:
    stuff = ET.parse(fname)
except:
    print('No such file or invalid file type.')
    quit()

tracks = stuff.findall('dict/dict/dict')

def lookup(entry, key):
    found = False
    for child in entry:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

cnt = 0
for track in tracks:
    track_title = lookup(track, 'Name')
    track_len = lookup(track, 'Total Time')
    track_rating = lookup(track, 'Rating')
    track_count = lookup(track, 'Play Count')

    artist_name = lookup(track, 'Artist')

    album_title = lookup(track, 'Album')

    genre_name = lookup(track, 'Genre')

    if track_title is None or artist_name is None or album_title is None or genre_name is None:
        continue

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?);', (artist_name, ))

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?);', (genre_name, ))

    cur.execute('SELECT id FROM Artist WHERE name=?;', (artist_name, ))
    artist_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?);', (album_title, artist_id))

    cur.execute('SELECT Album.id, Genre.id FROM Album JOIN Genre WHERE Album.title=? AND Genre.name=?;', (album_title, genre_name))
    ids = cur.fetchone()
    print(track_title, album_title, genre_name)
    album_id = ids[0]
    genre_id = ids[1]
    cur.execute('''
    INSERT OR UPDATE INTO Track (title, album_id, genre_id, len, rating, count)
    VALUES (?, ?, ?, ?, ?, ?);
    ''', (track_title, album_id, genre_id, track_len, track_rating, track_count))

conn.commit()
cur.close()
conn.close()
