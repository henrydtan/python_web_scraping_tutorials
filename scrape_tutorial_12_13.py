import urllib
from bs4 import BeautifulSoup
import urlparse

htmltext = urllib.urlopen("http://nytimes.com").read()
soup = BeautifulSoup(htmltext)

for tag in soup.findAll('a', href=True):
	raw = tag['href']
	b1 = urlparse.urlparse(tag['href']).hostname
	b2 = urlparse.urlparse(tag['href']).path
	newurl = "http://"+str(b1)+str(b2)
	print newurl

	# Python Web Crawler Tutorial 12
	# https://www.youtube.com/watch?v=LiAccbuBFwM
	
	# Python Web Crawler Tutorial 13
	# https://www.youtube.com/watch?v=bl6whQwdLXk