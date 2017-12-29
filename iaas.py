#!/usr/bin/python

import cgi
import commands
import cgitb
import thread
import time
import random
cgitb.enable()

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
os = data.getvalue('os')
ram = data.getvalue('ram')
cpu = data.getvalue('cpu')
passwd = data.getvalue('passwd')

port = str(5900+random.randrange(59100))

path = "/var/lib/libvirt/images/"

cmd0 = "sudo qemu-img create -f qcow2 -b "+path+os+".qcow2 "+path+"client"+os+".qcow2"

cmd1 = "sudo virt-install --name client"+os+"  --ram "+ram+" --vcpu "+cpu+" --disk path="+path+"client"+os+".qcow2 --import --graphics vnc,listen=127.0.0.1,port=5912,password="+passwd+" &>/dev/null"

cmd2 = "sudo websockify -D --web=/usr/share/novnc "+port+" 127.0.0.1:5912"

permission = "sudo chmod +x "+path+"client"+os+".qcow2"


def ok2():
	commands.getoutput(cmd0)
	commands.getoutput(permission)
	commands.getoutput(cmd2)
	commands.getoutput(cmd1)
thread.start_new_thread(ok2,())
time.sleep(6)

print "<body bgcolor='orange'>"
print "<h2>Your OS is Created</h2>"
print "<br><br>VNC Password : "+passwd
print "<br><br>OS username : sc-user"
print "<br><br>OS sc-user's password : 12345678"
print "<br><br>For Linux: Root Password : redhat"
print "<br><br><br>You can use VNC with VNC password to remote login using VNC<br><br>"
print "OR<br>"
print "<br>You can visit url : http://127.0.0.1:"+port+"/vnc_auto.html to use your OS from your browser<br>"
print "<br><a href='http://127.0.0.1:"+port+"/vnc_auto.html' target='_blank'><button>Go to your OS in browser</button></a>"
print "</body>"
#thread.start_new_thread(ok())
#username : sc-user
#password : 12345678

#username : root
#password : redhat


