import tweepy
import os
import sys

#pawan 
#access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
#access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
#consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
#consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"

#adish sir
access_token = "1222555806-0mO02HDbaEouGljkNEqZ1CxsXx0yFZ9UzYD00Aq"
access_token_secret = "0bqW6Xve3dyIpssqB2BqLJsMHfTQctXuNj3dKNpWFi1SK"
consumer_key = "guS93HPZ1uWICQ1NtEdxMv3dC"
consumer_secret = "I2zCD7lduZoCQCkzqeVByrvoCOloJfJv4lnBqUXG1BflR7S8vx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"


fh1=open(path+"SeedList.txt",'r')
fh2=open(path+"InitialID.txt",'a')
for handle in fh1:
	#print handle.strip()
	#handle=1222555806  #"adishw"#"mirwaizkashmir"#"PawanSingre"#BDUTT"#
	
	userinfo = api.get_user(handle) #PawanSingre
	fh2.write(str(userinfo.id)+"\n")
	#print userinfo.name
	#print userinfo.id  # 8 9 or 10 digit id
	#print userinfo.location
fh1.close()
fh2.close()
#fh.write(str(userinfo).encode('utf-8'))
#fh.write('\n') 
#print userinfo
