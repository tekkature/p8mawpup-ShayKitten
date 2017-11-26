# Subscriber_realtime
# I am so Confused about this project here is my code I got help from Gabriella in my class and Liam from your period 4 class. 
# This is all I have...

import time
import urllib
import re

htmlfile = urllib.urlopen("https://socialblade.com/youtube/user/mrsuicidesheep/realtime")
htmltext = htmlfile.read()
regex = '<p id="rawCount" style="display: none;">(.+?)</p>'	
pattern = re.compile(regex)
Subscribers = re.findall(pattern,htmltext)
print Subscribers

time.sleep(10)

htmlfile = urllib.urlopen("https://socialblade.com/youtube/user/mrsuicidesheep/realtime")
htmltext = htmlfile.read()
regex = '<p id="rawCount" style="display: none;">(.+?)</p>'	
pattern = re.compile(regex)
Subscribers = re.findall(pattern,htmltext)
print Subscribers
