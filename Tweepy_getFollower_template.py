import tweepy
import time
import wget
import os
import sys


consumer_key =
consumer_secret =
access_token = 
access_token_secret =


auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)


consumer_key =
consumer_secret = 
access_token = 
access_token_secret = 

auth2 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth2.set_access_token(access_token, access_token_secret)



consumer_key =
consumer_secret = 
access_token = 
access_token_secret = 

auth3 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth3.set_access_token(access_token, access_token_secret)


consumer_key =
consumer_secret = 
access_token = 
access_token_secret = 

auth4 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth4.set_access_token(access_token, access_token_secret)



api = tweepy.API(auth1,wait_on_rate_limit=True)

path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"
#fh1=open(path+"InitialID.txt",'r')

# in 1 minute we can get 5000 ids 
#ids = []
#count=0

#for handle in fh1:
#	fh2=open(path+"FollowerData/"+handle.strip(),'a')
#	for page in tweepy.Cursor(api.followers_ids, id=handle.strip()).pages():
#		for i in page:
#			fh2.write(str(i)+"\n")
#		time.sleep(60)
#	fh2.close()

#fh1.close()
lock=0

fh1=open(path+"InitialID.txt",'r')
for handle in fh1:
	if(not os.path.exists(path+"FollowerData/"+handle.strip())):
		continue
	fh2=open(path+"FollowerData/"+handle.strip(),'r')
	for nexthandle in fh2:
		if(os.path.exists(path+"FollowerData/"+nexthandle.strip())):
			continue
		
		fh3=open(path+"FollowerData/"+nexthandle.strip(),'a')
		flag=1
		while flag==1:
				
			try:
				#print nexthandle.strip()
				for page in tweepy.Cursor(api.followers_ids, id=nexthandle.strip()).pages():
					for i in page:
						fh3.write(str(i)+"\n")
					if len(page)>4090: 
						time.sleep(60)
				fh3.close()
				flag=0
				counter=0
				#print "success"
			except tweepy.TweepError as e:
				#print e
				try:
					if e[0][0]['code']==34:
						flag=0
					if e[0][0]['code']==88:
						#print sys.exc_info()[0]
						counter=counter+1
						if lock==0:
							api = tweepy.API(auth2,wait_on_rate_limit=True)
							lock=1
							time.sleep(2)
						elif lock==1:
							api = tweepy.API(auth3,wait_on_rate_limit=True)
							lock=2
							time.sleep(2)
						else:
							api = tweepy.API(auth1,wait_on_rate_limit=True)
							lock=0
							time.sleep(2)	
						if counter>3:
							time.sleep(120)
							counter=0
				except:
					flag=0
					#print "error"
					pass	

				#e.message[0]['code']
			
				
					
				#pass
	fh2.close()
	
fh1.close()


		

#print len(ids)



#for page in tweepy.Cursor(api.followers_ids, screen_name="adgpi").pages():

