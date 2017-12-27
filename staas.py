#!/usr/bin/python

import cgi
import commands
import cgitb

cgitb.enable()

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
s_type = data.getvalue('type')
name = data.getvalue('name')
size = data.getvalue('size')

cmd0 = "sudo lvcreate -V"+size+"G --name "+name+" --thin /dev/scloud/scloudpool"

cmd1 = "sudo mkfs.xfs /dev/scloud/"+name

cmd2 = "sudo mkdir /var/www/html/"+name

cmd3 = "sudo mount /dev/scloud/"+name+" /var/www/html/"+name

cmd4 = "sudo chmod 777 /var/www/html/"+name


print "Creating Disk...."
commands.getoutput(cmd0)
print "Formatting...."
commands.getoutput(cmd1)
print "Creating Directory...."
commands.getoutput(cmd2)
print "mounting...."
commands.getoutput(cmd3)
print "Permissioning..."
commands.getoutput(cmd4)

f1 = open("/etc/exports","a")
y = '/var/www/html/'+name+'  *(rw)\n'
f1.write(y)
f1.close()

commands.getoutput("sudo exportfs -r")

f2 = open("/var/www/html/"+name+"/"+name+".txt","w")
x = "#!/bin/bash\nsudo mkdir /mnt/"+name+"\nmount 192.168.43.2:/var/www/html/"+name+" /mnt/"+name
f2.write(x)
f2.close()
commands.getoutput("sudo chmod +x /var/www/html/"+name+"/"+name)
