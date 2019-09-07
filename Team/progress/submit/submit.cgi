#!/usr/local/bin/python3
import os, cgi, hashlib, io, re, mimetypes
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
	
try:
	files = []
	if i >= 0:
		for x in range (0, i + 1):
			file = form ['file' + str (x)]
			newfilename = '../custom_img/' + hashlib.sha1 (file.filename.encode()).hexdigest() + file.filename [file.filename.index ('.') :]
			try:
				with open (newfilename, 'wb') as savefile:
					savefile.write (file.file.read())
			except Exception as e:
				print ("Unable to save file")
				print (e)
			files.append (newfilename)
except Exception as e:
	print ("ERROR: Can't process files")
	print (e)
	exit()

try:
	userreq = os.environ ['REMOTE_USER']
except:
	print ("ERROR: Not authenticated!")
	exit()

if userreq != "menon18" and userreq != "agokan" and userreq != "kelley96" and userreq != "shankak":
	print ("ERROR: Not a valid user!")
	exit()

try:
	with open ('../' + userreq + '.html', 'r+', encoding="utf-8") as file:
		html = file.read()
except Exception as e:
	print ("ERROR: Cannot open HTML!")
	print (e)
	exit()

prog = re.sub (r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', prog)

newhtml = '                    <p class="text-left">' + prog.replace ('\n', '<br>') + '</p>\n'

for filepath in files:
	try:
		if 'webp' in filepath or 'image' in mimetypes.guess_type (filepath)[0]:
			newhtml += '                    <a href={0}><img class="insert_media" src="{0}"></a>\n'.format (filepath.replace ('../', ''))
		elif 'video' in mimetypes.guess_type (filepath)[0]:
			newhtml += '                    <video controls class="insert_media_vid"><source src="{0}" type="{1}"></video>\n'.format (filepath.replace ('../', ''), mimetypes.guess_type (filepath)[0])
	except Exception as e:
		print ("ERROR: Invalid file")
		print (e)
		pass

newhtml += '                    <div class="bordered" style="width: 100%"></div>\n'
html = html.replace ('                    <!--REPLACE HERE-->', newhtml + '                    <!--REPLACE HERE-->')

# try:
# 	repr (html.encode ('utf-8'))

# except Exception as e:
# 	print (e)

try:
	with open ('../' + userreq + '.html', 'wb') as file:
		file.write (html.encode ('utf-8'))
		print ("Page successfully updated!")
except Exception as e:
	print ("Error saving HTML to file.")
	print (e)