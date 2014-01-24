import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize


url = "http://sparkbrowser.com"
br = mechanize.Browser()
urls = [url]
visited = [url]
while len(urls) > 0:
	try:
		br.open(urls[0])
		urls.pop(0)
		for link in br.links():
			newurl = urlparse.urljoin(link.base_url,link.url)
			b1 = urlparse.urlparse(newurl).hostname
			b2 = urlparse.urlparse(newurl).path
			newurl =  "http://"+b1+b2

			if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
				urls.append(newurl)
				visited.append(newurl)
				print newurl
	except Exception:
			print "error"
			urls.pop(0)
print visited


# Python Webcrawler D3 Javascript Tutorial 16
# https://www.youtube.com/watch?v=UV21xHuYSE0

# In this tutorial, I also used wget to create a mirror for Area 51.
# mkdir wgotten
# wget -m http://adbnews.com/area51/index.html
# rm -r adbnews.com/

# Next
# https://www.youtube.com/watch?v=0jJMZ_hQ7I4