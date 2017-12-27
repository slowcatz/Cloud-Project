#!/usr/bin/python


import cgi
import MySQLdb


print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
user = data.getvalue('username')
passwd = data.getvalue('password')

if user==None or passwd==None:
	print "<script>alert('Username or Password cannot be Empty!!!');</script>"
	print '<meta http-equiv="refresh" content="0;url=http://127.0.0.1/homepage.html">'
	
db = MySQLdb.connect("localhost","root","redhat","cloud")
cursor = db.cursor()

cursor.execute("select password from profile where username='"+user+"'")
data = cursor.fetchone()

if data==None:
	print "No such user"
else:
	if passwd==data[0]:
		print '<meta http-equiv="refresh" content="0;url=http://127.0.0.1/cloudhome.html">'
	else:
		print "Wrong Password"
