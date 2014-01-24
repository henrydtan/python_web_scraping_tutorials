import urllib
import re
import json

symbolslist = open("symbols.txt").read()
symbolslist = symbolslist.split("\n")

for symbol in symbolslist:
	myfile = open("./daily_prices/" +symbol +".txt", "w+")
	myfile.close()
	
	htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+ symbol+ ":US")
	data = json.load(htmltext)
	datapoints = data["data_values"]
	
	myfile = open("./daily_prices/" +symbol +".txt", "a")
	for point in datapoints:
		myfile.write(str(symbol+","+str(point[0])+","+str(point[1])+"\n"))
	myfile.close()
	
		
# print datapoints[len(datapoints)-1][1]

# Python Web Scraping Tutorial 5 (Network Requests)
# https://www.youtube.com/watch?v=5FoSwMZ4uJg

# Python Web Scraping Tutorial 6 (Json Response)
# https://www.youtube.com/watch?v=qbEN3boz7_M

# Python Web Scraping Tutorial 7 (Getting 1 Minute Stock Data)
# https://www.youtube.com/watch?v=1RZRxJPVAC8

# Python Web Scraping Tutorial 8 (Free Stock Data)
# https://www.youtube.com/watch?v=5-OWLYyHUR0