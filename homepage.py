#!/usr/bin/python

import cgi

print "Content-type:text/html"
print ""
user=""
passwd=""
data = cgi.FieldStorage()
user = data.getvalue('username')
passwd = data.getvalue('password')

if user==None or passwd==None:
	print "<script>alert('Username or Password cannot be Empty!!!');</script>"
	
elif user == 'root' and passwd == 'redhat':
	print('<meta http-equiv="refresh" content="5;url=http://192.168.10.234/index.html">') 
	
else:
	print "Error"

