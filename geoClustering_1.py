import tweepy
import time
import wget
import os
import random
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')


#pawan
access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"
folder="OmarObdulah"#FollowerData"
userid={}
if(os.path.exists(path+folder+'/DoneIDs.txt')):
	f=open(path+folder+'/DoneIDs.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()


#InitialLen=len(userid)

if(os.path.exists(path+folder+'/DoneIDs_1.txt')):
	f=open(path+folder+'/DoneIDs_1.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()

print  len(userid)

count=0;
k=100

fname="138822469_1"
fullpath=path+folder+"/"



fh1=open(fullpath+'DoneIDs_1.txt', 'a')
newuserid=[]
InitialLen=0

#fh3=open(path+"adgpi", 'r')
#fh3=open(path+"InitialID_JnK.txt",'r')
#lines=fh3.readlines()

count=0
k=5

#folderarff="FollowerARFF/"

fullpath=path+folder+"/"
file_path_arff=fullpath+fname+'_.arff'
if(not os.path.exists(file_path_arff)):
	fd2=open(file_path_arff, 'a')
	fd2.write("@relation Location")
	fd2.write("\n\n@attribute id numeric \n")		
	fd2.write("@attribute userid numeric\n")
	fd2.write("@attribute screen_name string \n")
	fd2.write("@attribute name string\n")
	fd2.write("@attribute followers_count numeric\n")
	fd2.write("@attribute statuses_count numeric\n")
	fd2.write("@attribute friends_count numeric\n")
	#fd2.write("@attribute location string\n")
	fd2.write("@attribute favourites_count numeric\n")
	fd2.write("@attribute created_at string\n")
	fd2.write("@attribute location string\n")
	fd2.write("\n@data\n")

else :
	fd2=open(file_path_arff, 'a')

try:	
	f=open(fullpath+fname,'r')
	for handle in f:
		handle1=int(handle.strip())
		try:
			if userid[handle1]==0: 
				continue
		except:
			#print "ok"
			#newuserid.append(handle1)
			try:				
				udata = api.get_user(handle1) 
				fd2.write(str(udata.id)+","+str(udata.screen_name)+","+str(udata.name)+","+str(udata.followers_count)+","+str(udata.statuses_count)+","+str(udata.friends_count)+","+str(udata.favourites_count)+","+str(udata.created_at)+","+str(udata.location)+"\n")
				#count=count+1
				#if count>k:
				#	for i in range(InitialLen,len(newuserid)):
				fh1.write(str(handle1))
				fh1.write("\n")
				#	InitialLen=len(newuserid)
				#	k+=5	
			except tweepy.TweepError as e:
				print e
				try:	
					if e[0][0]['code']==88:	
						time.sleep(361)
						udata = api.get_user(handle1) 
						fd2.write(str(udata.id)+","+str(udata.screen_name)+","+str(udata.name)+","+str(udata.followers_count)+","+str(udata.statuses_count)+","+str(udata.friends_count)+","+str(udata.favourites_count)+","+str(udata.created_at)+","+str(udata.location)+"\n")
						#count=count+1
						#if count>k:
						#	for i in range(InitialLen,len(newuserid)):
						fh1.write(str(handle1))
						fh1.write("\n")
				except:
					pass
				pass
		
	f.close()
except :
	#print "error2"
	pass
#except tweepy.TweepError as e:
#	print e
#for i in range(InitialLen,len(newuserid)):#
#	fh1.write(str(newuserid[i]))
#	fh1.write("\n")
#InitialLen=len(userid)
fh1.close()
fd2.close()
