import tweepy
import os
import sys

#pawan
access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
all_tweets=[]
BasePath="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"

userinfo={}
if(os.path.exists(path+"Analysis/JnK_TwitterUsersData.txt")):
	f=open(path+"Analysis/JnK_TwitterUsersData.txt", 'r')
	lines = f.readlines()
	count=0
	for e in lines:	
		count+=1
		if count<=13:
			continue
	   	if data == '':
			break
	    	else:
		data=e.split(",")
		userinfo[int(data[0])]=int(data[4])
	f.close()



#thfd=open('/home/pawan/MTech2.1/MTP/MTPCode/tweet_AP_handle','r')
thfd=open(BasePath+"Analysis/JnK_TwitterUsersIDs.txt",'r')




flag=0
counttt=0
for handle in thfd:
	counttt+=1
		
	all_tweets=[]
	handle=handle.strip()
	if userinfo[int(handle)]==0:
		continue
	print counttt
	#tf = open(BasePath+'JnKTwitterCorpus/'+handle, 'a')
	file_path_arff=BasePath+'JnKTwitterCorpus/'+handle+'_arff.arff'
	if(not os.path.exists(file_path_arff)):
		fd2=open(file_path_arff, 'a')
		fd2.write("@relation "+handle)
		fd2.write("\n\n@attribute id numeric \n")		
		fd2.write("@attribute text string\n")
		fd2.write("@attribute created_at string\n")
		fd2.write("@attribute screen_name string \n")
		fd2.write("@attribute name string\n")
		fd2.write("@attribute followers_count numeric\n")
		fd2.write("@attribute statuses_count numeric\n")
		fd2.write("@attribute friends_count numeric\n")
		#fd2.write("@attribute location string\n")
		fd2.write("@attribute favourites_count numeric\n")
		fd2.write("@attribute retweeted string\n")
		fd2.write("@attribute retweet_count numeric\n")
		fd2.write("@attribute lang string\n")
		fd2.write("\n@data\n")
		
	else :
		continue
		#fd2=open(file_path_arff, 'a')	
	file_path=BasePath+'JnKTwitterCorpus/'+str(handle)+'_since_id'
	if(os.path.exists(file_path)):
		sidfd=open(file_path,'r')
		sid=long(sidfd.readline())
		flag=1
		sidfd.close()
	more=0
	if(flag==1):
		try:
			public_tweets=api.user_timeline(handle, count=100,since_id=sid) 
		except:
			print " proble1"
	else:
		try:
			public_tweets=api.user_timeline(handle, count=100) 
		except:
			print "proble2"
	
	
	
	for tweet in public_tweets:
		#tf.write(str(tweet).encode('utf-8'))
		#tf.write('\n') 
		text=tweet.text.strip().replace('\n',' ').replace('\r','').replace(',',' ').replace("'",'').replace('"','')
		try:
			date=str(tweet.created_at).split(' ')
			year=date[0].split('-')
			if int(year[0])<=2015:		
				more=1
				break
	
			fd2.write(str(tweet.id)+","+str(text.encode('utf-8'))+","+str(tweet.created_at)+","+str(tweet.author.screen_name).encode('utf-8')+","+str(tweet.author.name).encode('utf-8')+","+str(tweet.author.followers_count)+","+str(tweet.author.statuses_count)+","+str(tweet.author.friends_count)+","+str(tweet.author.favourites_count)+","+str(tweet.retweeted)+","+str(tweet.retweet_count)+","+str(tweet.lang)+"\n")
		except:
			print 'do nothing'
	if more==1:
		continue 	
	all_tweets.extend(public_tweets)
	#print "...%s tweets downloaded so far" % (len(all_tweets))
	if(len(public_tweets)>0):
		oldest = all_tweets[-1].id-1  
	
	while len(public_tweets) > 0:
		#print "getting tweets before %s" % (oldest)
		if(flag==1):
			try:
				public_tweets=api.user_timeline(handle, count=100,max_id=oldest, since_id=sid)
			except:
				print "proble3"
		else:
			try:
				public_tweets=api.user_timeline(handle, count=100,max_id=oldest) 
			except:
				print "proble4"
		for tweet in public_tweets:
			#tf.write(str(tweet).encode('utf-8'))
			#tf.write("\n")
			text=tweet.text.strip().replace('\n',' ').replace('\r','').replace(',',' ').replace("'",'').replace('"','')
			try:	
				date=str(tweet.created_at).split(' ')
				year=date[0].split('-')
				if int(year[0])<=2015:		
					more=1
					break
				fd2.write(str(tweet.id)+","+str(text.encode('utf-8'))+","+str(tweet.created_at)+","+str(tweet.author.screen_name).encode('utf-8')+","+str(tweet.author.name).encode('utf-8')+","+str(tweet.author.followers_count)+","+str(tweet.author.statuses_count)+","+str(tweet.author.friends_count)+","+str(tweet.author.favourites_count)+","+str(tweet.retweeted)+","+str(tweet.retweet_count)+","+str(tweet.lang)+"\n")
			except:
				print 'do nothing'
		if more==1:
			continue 
		all_tweets.extend(public_tweets)
		oldest = all_tweets[-1].id - 1
		#print all_tweets[-1].created_at
		#print "...%s tweets downloaded so far" % (len(all_tweets))
	if(len(all_tweets)):	
		sidfd=open(file_path,'w')
		sidfd.write(str(all_tweets[0].id + 1))
		sidfd.close()
	#tf.close()
	fd2.close()
thfd.close()
