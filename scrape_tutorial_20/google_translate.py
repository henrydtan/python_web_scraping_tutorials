import urllib
import mechanize


def translateString(home_language,target_language,text):
	text = text.replace(" ","%20")
	get_url = "http://translate.google.com/translate_a/t?client=t&sl="+home_language+"&tl="+target_language+"&hl="+home_language+"&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&ssel=3&tsel=0&q="+text
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent','Chrome')]
	translate_text = browser.open(get_url).read().decode("UTF-8")
	translate_text = translate_text.split("]]")
	translate_text = translate_text[0].replace("[[[","").replace('"','').split(",")
	return translate_text[0]







# https://www.youtube.com/watch?v=Igvf5C7qwO0
# Python Web Scraping Signature Series Tutorial 1 : Get Request with Python, Google Translate Part 1
