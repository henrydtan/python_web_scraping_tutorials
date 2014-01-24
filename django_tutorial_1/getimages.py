import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse

def getPic (search):
	try:
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders = [('User-agent','Mozilla')]

		htmltext = browser.open("https://www.google.com/search?q=cars&source=lnms&tbm=isch&sa=X&ei=PbGbUtqZNcbhoAT_o4AI&ved=0CAcQ_AUoAQ&biw=1264&bih=806")
		print htmltext
		img_urls= []
		soup = BeautifulSoup(htmltext)
		results = soup.findAll("a")
		for r in results:
			try:
				if "imgres?" in r['href']:
					img_urls.append(['href'])
			except:
					a = 0
		refer_url = urlparse(str(img_urls[0]))
		return refer_url.query.split("&")

	except:
		print "Oops, something went wrong!"

getPic("occupy wall street")


# Django Tutorial 1
# https://www.youtube.com/watch?v=ZAUNEEtzsrg
# Search images on google with python tutorial


# A regular HTTP request return this:
# <a href="http://www.google.com/imgres?sa=X&amp;biw=1264&amp;bih=806&amp;tbm=isch&amp;tbnid=B_XCO0CjizAPXM:&amp;imgrefurl=http://www.fanpop.com/clubs/sports-cars/images/13821367/title/farrari-wallpaper&amp;docid=uSmsJfiNVTS5tM&amp;imgurl=http://images2.fanpop.com/image/photos/13800000/farrari-sports-cars-13821367-1280-960.jpg&amp;w=1280&amp;h=960&amp;ei=UNCnUsq5H8zfkQf2w4DYCw&amp;zoom=1" class=rg_l ><img class=rg_i name=B_XCO0CjizAPXM: data-sz=f  onload="google.stb.csi.onTbn(1, this)"></a>


# <a href="/url?q=http://www.fanpop.com/clubs/sports-cars/images/13821367/title/farrari-wallpaper&amp;sa=U&amp;ei=kiipUoORKYOhkQfQlYDYBA&amp;ved=0CCoQ9QEwAA&amp;usg=AFQjCNEzVOPOamBHqzav6jjpzSTVv1b30g">