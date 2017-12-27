#!/usr/bin/python

import cgi
import MySQLdb
import cgitb

cgitb.enable()

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
fname = data.getvalue('fname')
lname = data.getvalue('lname')
user = data.getvalue('user')
pass1 = data.getvalue('pass1')
pass2 = data.getvalue('pass2')
email = data.getvalue('email')

if fname==None or lname==None or user==None or pass1==None or pass2==None or email==None:
	print "Please Fill All the fields"
	exit()
if pass1!=pass2:
	print "Cannot Confirm Password!!!"
	exit()

db = MySQLdb.connect("localhost","root","redhat","cloud")

cursor = db.cursor()

cursor.execute("select * from profile where username='"+user+"'")

data = cursor.fetchone()

if data==None:
	add = "insert into profile values('','"+fname+"','"+lname+"','"+user+"','"+pass1+"','"+email+"')"
	cursor.execute(add)
	db.commit()
	print "Registration Successful"
else:
	print "Username Taken"

