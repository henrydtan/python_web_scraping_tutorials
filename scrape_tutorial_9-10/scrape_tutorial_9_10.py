from threading import Thread
import urllib
import re
import MySQLdb

# Empty dictionary called gmap.
gmap = {}

# Open each link, convert to html, find pattern, and append results to dictionary.
def th(ur):
	base = "http://finance.yahoo.com/q?s="+ur
	regex = '<span id="yfs_l84_'+ur.lower()+'">(.+?)</span>'
	pattern = re.compile(regex)
	htmltext = urllib.urlopen(base).read()
	results = re.findall(pattern,htmltext)
	try:
		gmap[ur] = results[0]
	except:
			print "got an error"

symbolslist = open("symbols.txt").read()
symbolslist = symbolslist.replace("\n","").split(",")

print symbolslist

threadlist = []

for u in symbolslist:
	t = Thread(target = th, args = (u,))
	t.start()
	threadlist.append(t)

for b in threadlist:
	b.join()



"""
The below section is modified slightly from the tutorial.
I couldn't get the DB connection to work without "with."
"""
conn = MySQLdb.connect('localhost', 'root', 'password', 'mtf');
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS pywebscrape")
cur.execute("CREATE TABLE pywebscrape(symbol VARCHAR(255), last DOUBLE)")

with conn:
	for key in gmap.keys():
		print key, gmap[key]
		query = "INSERT INTO pywebscrape(symbol, last) VALUES("
		query = query + "'" + key + "',"+gmap[key]+")"
		cur.execute(query)
		row = cur.fetchall()


	
# Python Web Scraping Tutorial 9 (Multithreaded Python)
# https://www.youtube.com/watch?v=CXQ3QoT5bdQ

# Python MySQL Database Connection Tutorial 10
# https://www.youtube.com/watch?v=Mi9IAlqSwbE
