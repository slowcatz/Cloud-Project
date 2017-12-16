#!/usr/bin/python

import cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
if "saas" in data:
	print "<meta http-equiv='refresh' content='0;url=http://127.0.0.1/saas.html'>"
elif "iaas" in data:
	print "<meta http-equiv='refresh' content='0;url=http://127.0.0.1/iaas.html'>"
elif "paas" in data:
	print "<meta http-equiv='refresh' content='0;url=http://127.0.0.1/paas.html'>"
elif "staas" in data:
	print "<meta http-equiv='refresh' content='0;url=http://127.0.0.1/staas.html'>"
