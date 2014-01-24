import gethtml
import articletext
import google_translate
# import articletrans
import getarticle
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/2013/11/14/us/politics/democrats-threaten-to-abandon-obama-on-health-law-provision.html?hp&_r=0"

article_attrs = getarticle.getReadableArticle(url)
readable_article = article_attrs[0]
readable_title = article_attrs[1]

arabic = google_translate.translateString("en","ar",str(readable_article))
english = google_translate.translateString("ar","en",arabic)

# Google Translate Article Generator Python
# https://www.youtube.com/watch?v=jweHHc5nAwE