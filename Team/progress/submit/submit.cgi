#!/usr/local/bin/python3
import os, cgi, hashlib, io

form = cgi.FieldStorage()
print ("Content-Type: text/html\n\n")

i = -1
while 1:
	try:
		file = form ['file' + str (i + 1)]
		i += 1
	except:
		break

try:
	prog = form ['progress'].value
except:
	print ("ERROR: Please submit progress!")
	exit()
	
if i >= 0:
	files = []
	for x in range (0, i + 1):
		file = form ['file' + str (x)]
		newfilename = '../custom_img/' + hashlib.sha1 (file.filename.encode()).hexdigest() + file.filename [file.filename.index ('.') :]
		try:
			with open (newfilename, 'wb') as savefile:
				print ("Reading stream...")
				data = file.file.read()
				print ("Stream read...")
				savefile.write (data)
		except Exception as e:
			print ("Unable to save file")
			print (e)
		files.append (newfilename)

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

newhtml = '                    <p class="text-left">' + prog.replace ('\n', '<br>') + '</p>\n'
for filepath in files:
	newhtml += '                    <a href={0}><img class="insert_img" src="{0}"></a>\n'.format (filepath.replace ('../', ''))

newhtml += '                    <div class="bordered" style="width: 100%"></div>\n'
html = html.replace ('                    <!--REPLACE HERE-->', newhtml + '                    <!--REPLACE HERE-->')

print (html)

with open ('../' + userreq + '.html', 'w+') as file:
	file.write (html)
	print ("Page successfully updated!")
