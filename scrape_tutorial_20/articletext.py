from bs4 import BeautifulSoup
import gethtml

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('p'):
		try:
			articletext +=  str(tag.contents[0])
		except:
			a = 0
	return articletext

def getArticle(url):
	htmltext = gethtml.getHtmlText(url)
	return getArticleText(htmltext)

def getKeywords(articletext):
	common = open("common.txt").read().split("\n")
	word_dict = {}
	word_list = articletext.lower().split()
	for word in word_list:
		if word not in common and word.isalnum():
			if word not in word_dict:
				word_dict[word] = 1
			if word in word_dict:
				word_dict[word] += 1
	top_words =  sorted(word_dict.items(),key=lambda(k,v):(k,v),reverse=True)[0:25]
	top25 = []
	for w in top_words:
		top25.append(w[0])
	return top25


# Python Web Scraping Tutorial 18 : Keyword Generator
# https://www.youtube.com/watch?v=gpr6tbyKuyw