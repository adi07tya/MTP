import tweepy
import os
import sys
access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
all_tweets=[]

#thfd=open('/home/pawan/MTech2.1/MTP/MTPCode/tweet_AP_handle','r')
thfd=open('/home/pawan/MTech2.1/MTP/MTPCode/onehandle','r')
flag=0

for handle in thfd:
	all_tweets=[]
	handle=handle.strip()
	file_path='/home/pawan/MTech2.1/MTP/MTPCode/tweetcorpus_Search/'+str(handle)+'_since_id'
	if(os.path.exists(file_path)):
		sidfd=open(file_path,'r')
		sid=long(sidfd.readline())
		flag=1
		sidfd.close()

	if(flag==1):
		public_tweets=api.search(handle, count=100,since_id=sid) 
	else:
		public_tweets=api.search(handle, count=100) 
	tf = open('/home/pawan/MTech2.1/MTP/MTPCode/tweetcorpus_Search/'+handle, 'a')
	if(not os.path.exists(file_path)):
		fd2=open('/home/pawan/MTech2.1/MTP/MTPCode/tweetcorpus_Search/'+handle+'_arff.arff', 'a')
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
		fd2=open('/home/pawan/MTech2.1/MTP/MTPCode/tweetcorpus_Search/'+handle+'_arff.arff', 'a')

	for tweet in public_tweets:
		#tf.write(str(tweet.created_at)+"$$"+str(tweet.id)+"$$"+tweet.text.encode('utf-8')+"$$"+str(tweet.author.screen_name)+"\n")
		tf.write(str(tweet).encode('utf-8'))
		tf.write('\n') #+tweet.text.encode('utf-8')+"','"
		try:				
			text=tweet.text.strip().replace('\n',' ').replace('\r','').replace('.',' ').replace(',',' ').replace("'",'')
				
			fd2.write(str(tweet.id)+",'"+text.encode('utf-8')+"','"+str(tweet.created_at)+"','"+str(tweet.author.screen_name)+"','"+str(tweet.author.name)+"',"+str(tweet.author.followers_count)+","+str(tweet.author.statuses_count)+","+str(tweet.author.friends_count)+","+str(tweet.author.favourites_count)+",'"+str(tweet.retweeted)+"',"+str(tweet.retweet_count)+",'"+str(tweet.lang)+"'\n")
		except:
			print "do nothing"
		#fd2.write(str(tweet.id)+","+tweet.text+","+str(tweet.created_at)+","+tweet.author.screen_name+","+tweet.author.name+","+str(tweet.followers_count)+","+str(tweet.statuses_count)+","+str(tweet.friends_count)+","+tweet.location+","+str(tweet.favourites_count)+","+str(tweet.retweeted)+","+str(tweet.retweet_count)+"\n")
		
		#print tweet.text
		#print tweet.created_at	
		#print list1[0]
		#print list1[1]
		#print tweet.id
		#print tweet.author.screen_name
		#print "-------------------------------------------------"


	all_tweets.extend(public_tweets)
	print "...%s tweets downloaded so far" % (len(all_tweets))
	if(len(public_tweets)>0):
		oldest = all_tweets[-1].id  

	while len(public_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		if(flag==1):
			public_tweets=api.search(handle, count=100,max_id=oldest, since_id=sid) #adgpi the_hindu crpfindia
		else:
			public_tweets=api.search(handle, count=100,max_id=oldest) #adgpi the_hindu crpfindia	
		for tweet in public_tweets:
			#tf.write(str(tweet.created_at)+"$$"+str(tweet.id)+"$$"+tweet.text.encode('utf-8')+"$$"+str(tweet.author.screen_name)+"\n")
						
			tf.write(str(tweet).encode('utf-8'))
			tf.write("\n")
			try:
				text=tweet.text.strip().replace('\n',' ').replace('\r','').replace('.',' ').replace(',',' ').replace("'",'')
				fd2.write(str(tweet.id)+",'"+text.encode('utf-8')+"','"+str(tweet.created_at)+"','"+str(tweet.author.screen_name)+"','"+str(tweet.author.name)+"',"+str(tweet.author.followers_count)+","+str(tweet.author.statuses_count)+","+str(tweet.author.friends_count)+","+str(tweet.author.favourites_count)+",'"+str(tweet.retweeted)+"',"+str(tweet.retweet_count)+",'"+str(tweet.lang)+"'\n")
		
			except:
				print "do nothing"		
					
			#fd2.write(str(tweet.id)+","+tweet.text.encode('utf-8')+","+str(tweet.created_at)+","+str(tweet.author.screen_name)+","+str(tweet.author.name)+"\n")
		#	fd2.write(str(tweet.id)+","+tweet.text+","+str(tweet.created_at)+","+tweet.screen_name+","+tweet.name+","+str(tweet.followers_count)+","+str(tweet.statuses_count)+","+str(tweet.friends_count)+","+tweet.location+","+str(tweet.favourites_count)+","+str(tweet.retweeted)+","+str(tweet.retweet_count)+"\n")
		
		
		all_tweets.extend(public_tweets)
		oldest = all_tweets[-1].id - 1
		print all_tweets[-1].created_at
		print "...%s tweets downloaded so far" % (len(all_tweets))
	if(len(all_tweets)):	
		sidfd=open(file_path,'w')
		sidfd.write(str(all_tweets[0].id + 1))
		sidfd.close()
	tf.close()
	fd2.close()

#	e = sys.exc_info()[0]
#	print e
	
thfd.close()
