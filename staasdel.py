#!/usr/bin/python

import cgi,cgitb,commands

cgitb.enable()

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
name = data.getvalue('name')

f = open('/etc/exports','r')

x=[]
while True:
	d = f.readline()
	if len(d)==0:
		break
	if name+" " in d:
		continue
	x.append(d)
f.close()

f1 = open('/etc/exports','w')
for i in x:
	f1.write(i)

f1.close()
commands.getoutput("sudo exportfs -r")
commands.getoutput("sudo umount /var/www/html/"+name)
commands.getoutput("sudo rm -rf /var/www/html/"+name)
commands.getoutput("sudo lvremove /dev/scloud/"+name+" -y")
print "Done"
