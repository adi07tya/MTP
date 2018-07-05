import tweepy
import time
import wget
import os
import random
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

'''
#pawan
access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
'''

path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"
folder="OmarObdulah"#FollowerData"
userid={}
if(os.path.exists(path+folder+'/DoneIDs.txt')):
	f=open(path+folder+'/DoneIDs.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()


InitialLen=len(userid)

print "Initial length : "+str(InitialLen)
count=0
total=0
fname="138822469"
fullpath=path+folder+"/"
try:	
	f=open(fullpath+fname,'r')
	fname=file
	#print file
	for handle in f:
		handle1=int(handle.strip()) 
		total+=1	
		try:
			if userid[handle1]==0 : 
				continue
		
		except:
			count+=1
	f.close()
except:
	pass
print "Total : "+str(total)
print "remaining : "+str(count)
fname="138822469"
fh1=open(fullpath+fname+"_1",'a')
fh2=open(fullpath+fname+"_2",'a')
fh3=open(fullpath+fname+"_3",'a')		

try:	
	f=open(fullpath+fname,'r')
	#print file
	i=0
	fileselector=1
	for handle in f:
		handle1=int(handle.strip())
		try:
			if userid[handle1]==0 : 
				continue
		
		except:
			i+=1
			if i < int(count/3):
				if fileselector==1:
					fh1.write(str(handle1)+"\n")
				if fileselector==2:
					fh2.write(str(handle1)+"\n")
				if fileselector==3:
					fh3.write(str(handle1)+"\n")
					i=0
			else:
				if fileselector==1:
					i=0
					fh1.write(str(handle1)+"\n")
					fileselector=2
					continue	
				if fileselector==2:
					i=0
					fh2.write(str(handle1)+"\n")
					fileselector=3
				
						
	f.close()
except:
	pass	
fh1.close()
fh2.close()
fh3.close()


	
