#!/usr/bin/python

import cgi
import commands
import cgitb

cgitb.enable()

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
os = data.getvalue('os')
ram = data.getvalue('ram')
cpu = data.getvalue('cpu')
passwd = data.getvalue('passwd')

path = "/var/lib/libvirt/images/"

cmd0 = "sudo qemu-img create -f qcow2 -b "+path+os+".qcow2 "+path+"client"+os+".qcow2"

cmd1 = "sudo virt-install --name client"+os+"  --ram "+ram+" --vcpu "+cpu+" --disk path="+path+"client"+os+".qcow2 --import --graphics vnc,listen=127.0.0.1,port=5912,password="+passwd

permission = "sudo chmod +x "+path+"client"+os+".qcow2"

print cmd0

commands.getoutput(cmd0)
commands.getoutput(permission)
commands.getoutput(cmd1)

#username : sc-user
#password : 12345678

#username : root
#password : redhat


