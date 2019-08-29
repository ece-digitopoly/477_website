#!/usr/local/bin/python3
import os, cgi

print ("Content-Type: text/html\n\n")
print ("HERE")
try:
	prog = cgi.FieldStorage() ['progress'].value
except:
	print ("ERROR: Please submit progress!")
	exit()

try:
	userreq = os.environ ['REMOTE_USER']
except:
	print ("ERROR: Not authenticated!")
	exit()

if userreq != "menon18" and userreq != "agokan" and userreq != "kelley96" and userreq != "kelley96":
	print ("ERROR: Not a valid user!")
	exit()

with open ('../' + userreq + '.html', 'r') as file:
	html = file.read()

newhtml = '                    <p class="bordered text-left">' + prog.replace ('\n', '<br>') + '</p>\n'
html = html.replace ('<!--REPLACE HERE-->', newhtml + '<!--REPLACE HERE-->\n')

with open ('../' + userreq + '.html', 'w+') as file:
	file.write (html)
	print ("Page modified!")
