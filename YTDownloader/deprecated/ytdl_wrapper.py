# David Lau
# Youtube Playlist Downloader
# Wrapper for youtube-dl.exe
# Revision 2/15/15
# V1

import os
import pyperclip

link = "NULL"
d = 'n'
while(1):
	if(d == 'y'):
		break
	elif (d == 'n'):
		link = pyperclip.paste()
	try:
		print "Link is: " + link
	except:
		raw_input("Copy URL then press Enter\n")
		d = 'n'
		continue
	d = raw_input("Is the link correct? ('y' or 'n') OR (Ctrl+C to exit)\n")
d = os.getcwd()
#print "Current Directory: " + d
os.chdir(d+"/bin")
#print "New Directory: " + d
c = "youtube-dl.exe -o ../%(playlist)s/%(title)s.%(exts)s"+" --extract-audio --audio-format mp3 "+link
print "Executing Command: " + c
os.system(c)

raw_input("DONE")
