#!/usr/bin/python2.6
# conditionals, 
import argparse
import mysql.connector
# replace password with random pass 

__main__ = ""
password = ''
database = 'musictest'
user = 'musicadmin'
databases = []

def connect():
    conn = ""
    try:
        conn = mysql.connector.connect(host='localhost',
                                       user=user,
                                       password=password)
        if conn.is_connected():
            print 'Connected to MySQL database'
         
    except conn as e:
        print(e)
 
    finally:
        print 'OK'
        # conn.close()

def select_query():
    connect()
    conn = ""
    try:
	    database = "music"
	    conn = mysql.connector.connect(host='localhost',
					   user=user,
					   password=password,
					   database=database)
	    cur = conn.cursor()
	    cur.execute('SHOW DATABASES;')
	    # check if database exists. Create if not. 
	    print "Running query..."
	    for row in cur.fetchall():
		databases.append(row[0])
		    # cur.execute('CREATE DATABASE music;') 
    except conn as e:
        print "Error"
        print(e)

    finally:
        print 'OK'
        conn.close()

    return databases

def menu():
    playlist = ""
    playlist = raw_input("Playlist name: ")
    while playlist not in databases:
	print "Playlist %s not found" % playlist  
	playlist = raw_input("Playlist name: ")
	if playlist in databases:
	    print "Playlist %s found" % playlist
  
parser = argparse.ArgumentParser()
parser.add_argument("list_playlist")
args = parser.parse_args()

if args.list_playlist:
    select_query()
    menu()

