'''
	Code Function For Local Twitter Bot
'''
import tweepy
import pycorpora
import random

from KyttenCredentials import *
from KyttenPycorpora import *
from KyttenEasterEggs import *

def pycorpora_categories():
	'''Prints Corpora Categories
	'''
	kytten_gories = pycorpora.get_categories()
	print (kytten_gories)
	return kytten_gories

def kytten_api():
	'''
	API Keys & Tokens
	'''
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token_key, access_token_secret)
	api = tweepy.API(auth)
	return

def kytten_lookup():
	'''
	Returns Twitter ID # From screen name in KyttenCredentials.py
	'''
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token_key, access_token_secret)
	api = tweepy.API(auth)
	
	# Screen name is sourced from KyttenCredentials.py
	kytten_user = api.get_user(kytten_name)	
	kytten_id = kytten_user.id 
	print (kytten_id)
	return kytten_id


	return clowder

#def kytten_id()
def kytten_reply():
	'''
	Scans account mentions & replies to inqurer
	'''
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token_key, access_token_secret)
	api = tweepy.API(auth)
	
	#Pulls up most recent mention
	mention = api.mentions_timeline(count = 1)
	
	# Scans mention for keywords
	for body in mention:
		print(body.text)
		print(body.user.screen_name)
		
		# Easter eggs
		if "cake" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + cake)
		if "answer" in body.text:
			api.update_status("@"| body.user.screen_name + " " + answer)

		# Corpora Replies
		if "music" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + random.choice(genres))
		
		if "toxic" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + random.choice(toxic))
		
		if "surveillance" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(watching)))
		
		if "secret" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(secret)))
		
		if "names" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(GD)))
		
		if "fibonnaci" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(fib_num)))
		
		if "mood" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(mood)))
		
		if "gentrify" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(gentrify)))
		
		if "plant" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(plant)))

		if "420" in body.text:
			api.update_status("@"+ body.user.screen_name + " " + str(random.choice(legalize)))

		# Account Information Inquiries: Replies Twitter ID
		if "id" in body.text:
			api.update_status("@"+ body.user.screen_name + " your id: " + str(body.user.id))
	
	return

pycorpora_categories()
kytten_lookup()
kytten_reply()