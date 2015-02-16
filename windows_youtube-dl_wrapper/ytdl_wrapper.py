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
		raw_input ("Copy URL then press Enter\n")
		link = pyperclip.paste()
	print "Link is: " + link
	d = raw_input("Is the link correct? ('y' or 'n') OR (Ctrl+C to exit)\n")

os.system("youtube-dl.exe --extract-audio --audio-format mp3 "+link)

raw_input("DONE")
