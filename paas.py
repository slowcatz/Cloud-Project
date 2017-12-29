#!/usr/bin/python

import cgi,cgitb
import commands
import random

cgitb.enable()

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
lang = data.getvalue('lang')

cmd = ""

port = str(random.random())[-4:]

if lang=='python':
	cmd = "sudo docker run -itd -p "+port+":4200 project0"
	print commands.getoutput(cmd)
	print "Use Port : "+port
	print "Username : python"
	print "Password : 123"
