import sys
import subprocess
import os
import time
import re
import glob


#Print Arguments

#Build exec command for youtube-dl
exec_cmd = list(sys.argv)
exec_cmd[0] = "youtube-dl.exe"
#print exec_cmd
lname = exec_cmd[len(exec_cmd)-1]
exec_cmd[len(exec_cmd)-1] = "--simulate"
exec_cmd.append("--get-filename")
exec_cmd.append("--get-url")
exec_cmd.append("--ignore-errors")
exec_cmd.append(lname)

print("Building link-list, this may take some time")
sys.stdout.flush()

# Open Temp File
x = 0
while(os.path.exists("temp"+str(x))):
	x+=1
fname = "temp"+str(x)
print "Opening: "+fname
# Run Sub Process
with open(fname, "w") as output:
	sproc = subprocess.Popen(exec_cmd, stdout=output)

#Notify User of Progress
while(sproc.returncode == None):
	print "."
	sys.stdout.flush()
	time.sleep(1)
	sproc.poll()

output.close()

output = open(fname, "r")
linkList = list()
nameList = list()
i = 0
for l in output:
	#print "line " + str(i) + " " + l
	if(i%2==0):
		linkList.append(l.rstrip())
	else:
		nameList.append(l.rstrip())#re.sub(r'\s+','',l.rstrip()))
	i+=1

output.close()

#debug print lists
#print nameList
#print linkList

cdir = os.getcwd()
pdir = os.path.dirname(cdir)

#build aria input file
iname = fname+"i"
input = open(iname, "w")
for i in range(0,len(linkList)):
	input.write(linkList[i])
	input.write("\n")
	input.write("  "+"out="+nameList[i])
	input.write("\n")
input.close()

#Make Aria Call with temp file
exec_aria = list()
exec_aria.append("aria2c.exe")
exec_aria.append("--dir="+pdir+"/downloads")
exec_aria.append("--max-concurrent-downloads=10")
exec_aria.append("--max-connection-per-server=16")
exec_aria.append("--input-file="+iname)
#print exec_aria

aria_proc = subprocess.Popen(exec_aria)
aria_proc.wait()

os.remove(fname)
os.remove(iname)


# Convert M4A to MP3
"""
workdir = pdir+"/downloads/"
exec_ffmpeg = list()
exec_ffmpeg.append("ffmpeg.exe")
exec_ffmpeg.append("-i")
exec_ffmpeg.append("INPUT_FILE")
exec_ffmpeg.append("-acodec")
exec_ffmpeg.append("libmp3lame")
exec_ffmpeg.append("-ab")
exec_ffmpeg.append("128k")
exec_ffmpeg.append("OUTPUT_FILE")
for file in glob.glob(workdir+"*.m4a"):
	#print("Must convert: " + file)
	out = re.sub(".m4a", ".mp3", file)
	if(os.path.exists(out)):
		print out + "already exists, skipping"
		os.remove(file)
		continue
	exec_ffmpeg[2] = file
	exec_ffmpeg[7] = out
	ffmpeg_proc = subprocess.Popen(exec_ffmpeg)
	ffmpeg_proc.wait()
	#remove the m4a file
	os.remove(file)

"""
print "DONE - Ready for next job"




