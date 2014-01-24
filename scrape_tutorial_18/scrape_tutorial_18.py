# articletext.py
# gethtml.py

import gethtml
import articletext

url = "http://www.va-clients.com/veros_website_v6/method.html"

article = articletext.getArticle(url)

print articletext.getKeywords(article)


# Python Web Scraping Tutorial 18 : Keyword Generator
# https://www.youtube.com/watch?v=gpr6tbyKuyw