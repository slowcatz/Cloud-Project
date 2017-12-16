#!/usr/bin/python

import cgi

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
	print "Please fill all the fields<br><br>"
	print "<a href=/html/register.html>Click here to go back</a>"





