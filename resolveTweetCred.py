import tweepy
import time
import wget
import os
import sys

#pawan singre 
#access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
#access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
#consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
#consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"


#sahil
consumer_key ="0gJKKyXscmsXOfPVdMFu0rD5u"
consumer_secret = "Pof0NF9X5aOGypoz3osdvgOz6Sp7KbReiLRJ4ljsONcIndH34y"
access_token = "1525179444-clyR2Y8hHU0ckeXsm5MzTwFdFKehgLeO40ktxnV"
access_token_secret = "4euhYSdGGss1HjyUb9h2WNwi0xt0pwBXikyT9xscR1MXF"

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth1)
#tweet="SC asks producer of upcoming film #JollyLLB2 to go to #Bombay HC against earlier order appointing a panel to review the movie"
#tweet="Yes this is a fake news to confuse people"
#tweet="Capt Jaideep undaunted by wounds maintained pressure on enemy,pinning them down by fire , displayed conspicuous courage, awarded"
tweet="social undaunted awarded"
#tweet= "Its time for us to modernize our army personals with proper gear, its our responsibility to protect them who protect us"
#tweet="A friend whatsapped this to me this morning. Perfect timing. It's exactly how Monday mornings often startle me after a peaceful weekend"
#tweet="Year made memorable innocent smiles"
print tweet

stopwords={}
path="/home/pawan/MTech2.2/MTP/MTPCodeData/FakeNews/"
fname="StopwordList.txt"

fh1=open(path+fname,'r')
for word in fh1:
	stopwords[word.strip()]=0

allwords=tweet.lower().split()
keywords=[]
handle=""
for key in allwords:
		try:
			if stopwords[key]==0:
				continue
		except:
			keywords.append(key)
			handle+=" "+key

print handle
print
try:
	public_tweets=api.search(handle, count=1)
	for tweet in public_tweets:
		wlist=tweet.text.split()		
	if wlist[0]=="RT":
		handle=wlist[1].split(':')
		print handle[0]
		userinfo = api.get_user(handle[0]) #PawanSingre
		#fh=open("/home/pawan/MTech2.2/MTP/MTPCodeData/UserDataTwitter/"+handle+".txt",'a')
		print userinfo.name
		print userinfo.screen_name
		print "Id :" +str(userinfo.id)  # 8 9 or 10 digit idfollowers_count
		print "Location :" +userinfo.location
		print "Follower Count : "+str(userinfo.followers_count)
		print "Friends Count : "+str(userinfo.friends_count)
		print "verified :" + str(userinfo.verified)
		if(userinfo.verified==True):
			print "Trusted Tweet : Originated account is verified"
			
	if(len(public_tweets)>0):
		oldest = tweet.id 
	
	#while len(public_tweets) > 0:
	#	print "getting tweets before %s" % (oldest)
	#	public_tweets=api.search(handle, count=100,max_id=oldest) #adgpi the_hindu crpfindia	
	#	for tweet in public_tweets:
		 
except tweepy.TweepError as e:
	print e




	

	 	
