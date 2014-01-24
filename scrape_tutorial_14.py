import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize


url = "http://adbnews.com/area51/contact.html"

br = mechanize.Browser()

br.open(url)

for link in br.links():
	newurl = urlparse.urljoin(link.base_url,link.url)
	b1 = urlparse.urlparse(newurl).hostname
	b2 = urlparse.urlparse(newurl).path
	print "http://"+b1+b2


"""
url = "http://sparkbrowser.com"

htmlfile = urllib.urlopen(url)

soup = BeautifulSoup(htmlfile)

for tag in soup.findAll('a',href=True):
	print urlparse.urlparse(tag['href']).path
"""

"""
url = "http://adbnews.com/area51"
base = 'http://adbnews.com/area51'

htmlfile = urllib.urlopen(url)

soup = BeautifulSoup(htmlfile)

for tag in soup.findAll('a', href=True):
	print base+"/"+tag ['href']
"""

"""
url = "http://adbnews.com/area51"

htmlfile = urllib.urlopen(url)

soup = BeautifulSoup(htmlfile)

for tag in soup.findAll('a', href=True):
	print tag ['href']
"""

# Python MechanizeTutorial 14
# https://www.youtube.com/watch?v=p4dOPXWaeLI

# Next
# Python WebCrawler Tutorial 15
# https://www.youtube.com/watch?v=zjrttArGSoU