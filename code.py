#coding: utf-8
import time
import urllib
import re

def main():
  while True:
    
   htmlfile = urllib.urlopen("https://socialblade.com/youtube/user/mrsuicidesheep/realtime")
   htmltext = htmlfile.read()
   regex = '<p id="rawCount" style="display: none;">(.+?)</p>'	
   pattern = re.compile(regex)
   Subscribers = re.findall(pattern,htmltext)
   print Subscribers
   time.sleep(10)

if __name__ == "__main__":
  main()
	



