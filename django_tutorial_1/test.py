
import urllib
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("https://www.google.com/search?q=cars&source=lnms&tbm=isch&sa=X&ei=PbGbUtqZNcbhoAT_o4AI&ved=0CAcQ_AUoAQ&biw=1264&bih=806").read()
soup = BeautifulSoup(htmltext)
print soup