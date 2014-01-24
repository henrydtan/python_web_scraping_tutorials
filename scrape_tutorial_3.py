import urllib
import re


symbolslist = ["aapl","thrx","aamrq","azc", "wag"]


i=0
while i<len(symbolslist):
	url = "http://finance.yahoo.com/q?s=" +symbolslist[i] +"&ql=1"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_'+symbolslist[i] +'">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern, htmltext)
	print "the price of",symbolslist[i]," is " ,price
	i+=1
	
	
# Python Web Scraping Tutorial 3 (Downloading Stock Data)	
# https://www.youtube.com/watch?v=f2h41uEi0xU