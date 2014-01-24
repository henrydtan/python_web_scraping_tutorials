from bs4 import BeautifulSoup
import gethtml

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('a',attrs={"class":"yt-uix-sessionlink yt-uix-tile-link yt-uix-contextlink yt-ui-ellipsis yt-ui-ellipsis-2"}):
		articletext +=  tag.contents[0]
	return articletext

def getArticle(url):
	htmltext = gethtml.getHtmlText(url)
	return getArticleText(htmltext)
