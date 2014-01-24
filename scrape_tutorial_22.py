from twython import Twython

TWITTER_APP_KEY = '6t34eQuAov9E2ZD9sKA44w'
TWITTER_APP_KEY_SECRET = 'vpf7t2oqf8MP5mr149ggH5DMDuOVRALw648MFQHk'
TWITTER_ACCESS_TOKEN = '239647734-vlrrIVlN6R6W2sJTdQhAJuuwYLEDNax6Bko5Zpve'
TWITTER_ACCESS_TOKEN_SECRET = 'Q94lJxyTlCWYJQ4gto4Du1qOnE9fg3HWOJMVkEoUM5VXx'

t = Twython(app_key = TWITTER_APP_KEY, app_secret = TWITTER_APP_KEY_SECRET, oauth_token = TWITTER_ACCESS_TOKEN, oauth_token_secret = TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q = 'xolair', count = 100)

tweets = search['statuses']

for tweet in tweets:
	print tweet['text'], "\n"
	# print tweet ['id_str'], '\n', tweet['text'], '\n\n\n'