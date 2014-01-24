import nltk
import urllib
import readability
from bs4 import BeautifulSoup
import mechanize
from readability.readability import Document


def getReadableArticle(url):

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]

	html = br.open(url).read()

	readable_article = Document(html).summary()
	readable_title = Document(html).short_title()

	soup = BeautifulSoup(readable_article)

	final_article = soup.text

	links  = soup.findAll('img', src=True)

	return [final_article, readable_title]




# Python Web Scraping Tutorial 19 : Python Content Generator
# https://www.youtube.com/watch?v=Edd4B8ZtY4E

# Downloaded readability https://github.com/buriy/python-readability
# Downloaded nltk