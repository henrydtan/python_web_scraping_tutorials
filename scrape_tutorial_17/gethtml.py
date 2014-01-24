import mechanize

def getHtmlText(url):
	br = mechanize.Browser()
	htmltext = br.open(url).read()
	return htmltext

def getHtmlFile(url):
	br = mechanize.Browser()
	htmltext = br.open(url)
	return htmltext

# Article Scraping in Python web scraping tutorial 17
# https://www.youtube.com/watch?v=0jJMZ_hQ7I4