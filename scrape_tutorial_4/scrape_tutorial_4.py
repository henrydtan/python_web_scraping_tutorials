import urllib
import re

symbolfile = open ("symbols.txt")

symbolslist = symbolfile.read()

newsymbolslist =  symbolslist.split("\n")

i=0
while i<len(newsymbolslist):
	url = "http://finance.yahoo.com/q?s=" +newsymbolslist[i] +"&ql=1"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern, htmltext)
	print "the price of",newsymbolslist[i]," is " ,price
	i+=1
	
	
# Python Web Scraping Tutorial 4 (Downloading Every Stock Price)	
# https://www.youtube.com/watch?v=Mjjt__c4syY