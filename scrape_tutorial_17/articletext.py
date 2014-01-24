from bs4 import BeautifulSoup
import gethtml

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('p',attrs={"itemprop":"articleBody"}):
		articletext +=  tag.contents[0]
	return articletext

def getArticle(url):
	htmltext = gethtml.getHtmlText(url)
	return getArticleText(htmltext)

# Article Scraping in Python web scraping tutorial 17
# https://www.youtube.com/watch?v=0jJMZ_hQ7I4