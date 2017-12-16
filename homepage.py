#!/usr/bin/python

import cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
user = data.getvalue('username')
passwd = data.getvalue('password')

if user==None or passwd==None:
	print "<script>alert('Username or Password cannot be Empty!!!');</script>"
	print('<meta http-equiv="refresh" content="0;url=http://127.0.0.1/homepage.html">') 
	
elif user == 'root' and passwd == 'redhat':
	print('<meta http-equiv="refresh" content="0;url=http://127.0.0.1/cloudhome.html">') 
	
else:
	print "Error"
