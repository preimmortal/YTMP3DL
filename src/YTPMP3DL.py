from lxml import html
import requests

import os
import subprocess
import time

# Ask for Page URL
# raw_page = raw_input("Enter web page URL: ")

# Build Page Tree
page = requests.get('https://www.youtube.com/playlist?list=PL_ktuxZNJnpiEsZVxaXxmOQTEG6245Iw7')
tree = html.fromstring(page.text)

# Get Videos in playlist
videos = tree.xpath('//a[@class="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "]/text()')

# //td[@class='name']/a/@href|//td[@class='name']
vidlinks = tree.xpath('//a[@class="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "]/@href')


# debug prints, print all vids + links
print "Number of Videos: " + str(len(videos))
linkList = list()
YTBASEADDR = "https://www.youtube.com"
for i in range (0, len(videos)):
    print str(i) + " " + videos[i] + " " + vidlinks[i]
    linkList.append(YTBASEADDR+vidlinks[i])

# build link list
f = open("playlist.txt", "w")
for l in linkList:
    #print l
    #os.system(("youtube-dl" + " --no-playlist --extract-audio --audio-format mp3 "+l))
    #time.sleep(10)
    f.write(l+"\n")
f.close()


os.system("youtube-dl --extract-audio --audio-format mp3 --batch-file playlist.txt")


