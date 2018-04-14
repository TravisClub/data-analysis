import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key='DE8WLnHXz4ylHLEAmkBbpVwW9'
consumer_secret='R0dP6oP42vcPhgKdxij2WmDM9zpbRRNTOk5RTBJjEyygjV0dtP'
access_token='946061385246617601-2iGwKqHM5wYPRicADbXdsCAxcOPmBfn'
access_token_secret='9MneENG5YuvLtF97be9Qt7xRY47EXP2XU05RmBiSru0FI'

# 2.1 Authentication piece
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# 2.2 Stream Handler

class PrintListener(StreamListener):
	def on_status(self, status):
		if not status.text[:3] == 'RT: ':
			print(status.text)
			print(status.author.screen_name, status.created_at, status.source, '\n')

	def on_error(self, status_code):
		print("Error code: {}".format(status_code))
		return True # keep stream alive

	def on_timeout(self):
		print('Listener timed out!')
		return True # keep stream alive

# 2.3 Access twitter data stream

def print_to_terminal():
	listener = PrintListener()
	stream = Stream(auth, listener)
	languages = ('en',)
	stream.sample(languages=languages)


def pull_down_tweets(screen_name):
	api = API(auth)
	tweets = api.user_timeline(screen_name=screen_name, count=200)
	for tweet in tweets:
		print(json.dumps(tweet._json, indent=4))

if __name__ == '__main__':
	# print_to_terminal()
	pull_down_tweets(auth.username)