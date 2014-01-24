import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'password', 'mtf');

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS pywebscrape")
    cur.execute("CREATE TABLE pywebscrape(symbol VARCHAR(25))")
    cur.execute("INSERT INTO pywebscrape(symbol) VALUES('AAPL')")
    cur.execute("INSERT INTO pywebscrape(symbol) VALUES('AZC')")
    cur.execute("INSERT INTO pywebscrape(symbol) VALUES('GOOG')")
    cur.execute("INSERT INTO pywebscrape(symbol) VALUES('THRX')")
    cur.execute("INSERT INTO pywebscrape(symbol) VALUES('GLD')")
