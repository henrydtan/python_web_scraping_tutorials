import mechanize

def getHtmlText(url):
	br = mechanize.Browser()
	htmltext = br.open(url).read()
	return htmltext

def getHtmlFile(url):
	br = mechanize.Browser()
	htmltext = br.open(url)
	return htmltext

# Python Web Scraping Tutorial 18 : Keyword Generator
# https://www.youtube.com/watch?v=gpr6tbyKuyw