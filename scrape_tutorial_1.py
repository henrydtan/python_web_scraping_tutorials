import urllib
import re

urls = ["http://google.com", "http://youtube.com", "http://nytimes.com", "http://cnn.com", "http://facebook.com"]
i=0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i< len(urls):

	htmlfile = urllib.urlopen (urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	
	print titles
	i+=1


# Python Web Scraping Tutorial 2 (Getting Page Source)	
# https://www.youtube.com/watch?v=E7wB__M9fdw