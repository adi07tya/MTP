import tweepy
import time
import wget
import os
import random
access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
'''
followers=api.followers(ISPR_Official)
#public_tweets = api.home_timeline()
for tweet in follower:
	print tweet.text
	print tweet.created_at
	print tweet

print '-----------------------------------------------------------\n\n'
'''
#users = tweepy.Cursor(api.followers, screen_name='adgpi').items()
#fh=open('ADGPI_follower_list','a')

path="/home/pawan/MTech2.2/MTP/MTPCodeData/RandomAgeAnalysis/First10000/"

f=open(path+'allIDs', 'r')
lines = f.readlines()
userid =[int(e.strip()) for e in lines]
f.close()
InitialLen=len(userid)

fd2=open(path+"random.json", 'a')
count=0;
k=500

fh=open(path+'allIDs', 'a')

while True:
    try:
	handle=random.randrange(10**8, 10**10)
	if handle in userid: 
		continue
	userid.append(handle)		
	udata = api.get_user(handle)
	
        #udata = next(users)
	fd2.write('{"id":'+str(udata.id).encode('utf-8')+',"screen_name":"'+str(udata.screen_name).encode('utf-8')+'","name":"'+str(udata.name).encode('utf-8')+'","followers_count":'+str(udata.followers_count)+',"statuses_count":'+str(udata.statuses_count)+',"friends_count":'+str(udata.friends_count)+',"favourites_count":'+str(udata.favourites_count)+'}\n')
	list1=udata.profile_image_url.split("_")
	str1=udata.profile_image_url.replace("_normal","")
	fname=wget.download(str1)
	
	#print fname
	cmd='mv '+fname+' '+udata.screen_name 
	os.system(cmd)
	count=count+1
	#if count == k:
	#	#print count 
		#k=K+100
	if count>k:
		for i in range(InitialLen,len(userid)):
			fh.write(str(userid[i]))
			fh.write("\n")
		InitialLen=len(userid)
		k+=500	
	if count>10000:
		for i in range(InitialLen,len(userid)):
			fh.write(str(userid[i]))
			fh.write("\n")
		InitialLen=len(userid)
		break;
	#print handle	
       # time.sleep(60*15)
    except:
	pass
	
	
    #fh.write(str(user).encode('utf-8'))
    #fh.write('\n')	
    #print user.id

fd2.close()


f.close()

#fh.close()

'''
public_tweets=api.user_timeline('justinbieber')#'potus')justinbieber
for tweet in public_tweets:
	print tweet.text
	print tweet.created_at	
http://abs.twimg.com/sticky/default_profile_images/default_profile_1_normal.png
'''
'''
print "-------------------------------------------"
print "\n"
tf = open('tweets4.txt', 'w')
public_tweets=api.search('#indianarmy #kashmir', until='2016-08-23')
#public_tweets=api.search('#indianarmy #kashmir',count=100) #lang='en'
for t in public_tweets:
	print t.created_at
	print t.text
	tf.write(str(t.created_at))
	tf.write("\n")
	tf.write(t.text.encode('utf-8'))
	tf.write("\n")
#api.update_status("hi")
'''
