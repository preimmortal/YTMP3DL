from lxml import html
import requests

# Ask for Page URL
# raw_page = raw_input("Enter web page URL: ")

# Build Page Tree
page = requests.get('https://www.youtube.com/playlist?list=PL_ktuxZNJnpiEsZVxaXxmOQTEG6245Iw7')
tree = html.fromstring(page.text)

# Get Videos in playlist
videos = tree.xpath('//a[@class="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "]/text()')

# //td[@class='name']/a/@href|//td[@class='name']
vidlinks = tree.xpath('//a[@class="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "]/@href')




print "Number of Videos: " + str(len(videos))

for i in range (0, len(videos)):
    print str(i) + " " + videos[i] + " " + vidlinks[i]


print "Try This: " + "https://www.youtube.com" + vidlinks[0]

