import urllib
import re

htmltext =  urllib.urlopen("https://www.google.com/finance?q=thrx").read()

regex = '<span id="ref_[^.]*_l">(.+?)</span>'

pattern = re.compile(regex)

results = re.findall(pattern,htmltext)

print results