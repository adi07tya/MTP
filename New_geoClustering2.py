import tweepy
import time
import wget
import os
import random
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

#sahil
consumer_key ="0gJKKyXscmsXOfPVdMFu0rD5u"
consumer_secret = "Pof0NF9X5aOGypoz3osdvgOz6Sp7KbReiLRJ4ljsONcIndH34y"
access_token = "1525179444-clyR2Y8hHU0ckeXsm5MzTwFdFKehgLeO40ktxnV"
access_token_secret = "4euhYSdGGss1HjyUb9h2WNwi0xt0pwBXikyT9xscR1MXF"


auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)


#Adish Sir
access_token = "1222555806-0mO02HDbaEouGljkNEqZ1CxsXx0yFZ9UzYD00Aq"
access_token_secret = "0bqW6Xve3dyIpssqB2BqLJsMHfTQctXuNj3dKNpWFi1SK"
consumer_key = "guS93HPZ1uWICQ1NtEdxMv3dC"
consumer_secret = "I2zCD7lduZoCQCkzqeVByrvoCOloJfJv4lnBqUXG1BflR7S8vx"

auth2 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth2.set_access_token(access_token, access_token_secret)


#mansi
access_token = "3102633373-jHTcKBXmp4Agge4mBJPCnP5DluQ6UMyUnY0MZOB"
access_token_secret = "44pCj2ZlJk9B11VyV8a2jDXJhrQZvlJIQIyoU3NDoEGxW"
consumer_key = "aUdIoNXtBl0qYzMOIdAV4GlmE"
consumer_secret = "1MRH7LgpjuCWIOFy0GVzrOTVmH3e3El1Hgsg2lEcOyMiX0mK6L"

auth3 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth3.set_access_token(access_token, access_token_secret)



#pawan
access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"

auth4 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth4.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth1)
path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"
folder="New_FollowerData"
userid={}
if(os.path.exists(path+'DoneIDs.txt')):
	f=open(path+'DoneIDs.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()


if(os.path.exists(path+'DoneIDs_1.txt')):
	f=open(path+'DoneIDs_1.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()

if(os.path.exists(path+'DoneIDs_2.txt')):
	f=open(path+'DoneIDs_2.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()
if(os.path.exists(path+'DoneIDs_3.txt')):
	f=open(path+'DoneIDs_3.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()


if(os.path.exists(path+'DoneIDs_4.txt')):
	f=open(path+'DoneIDs_4.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()

if(os.path.exists(path+'DoneIDs_5.txt')):
	f=open(path+'DoneIDs_5.txt', 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()


InitialLen=len(userid)

fh1=open(path+'DoneIDs_5.txt', 'a')
fh3=open(path+'separate.txt', 'a')

#fh3=open(path+"adgpi", 'r')
#fh3=open(path+"InitialID_JnK.txt",'r')
#lines=fh3.readlines()

count=1
k=50
lock=0
folderarff="FollowerARFF/"

fullpath=path+folder+"/"
for fname in os.listdir(fullpath):
	#img_url ='/home/pawan/MTech2.1/MTP/MTPCode/FaceAPI/ad.jpg' #'https://raw.githubusercontent.com/Microsoft/indows/master/Data/detection1.jpg'
	
	file_path_arff=path+folderarff+fname+'_.arff'
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
		continue
		#fd2=open(file_path_arff, 'a')
	
	try:	
		try:				
			pcount=0
			udata = api.get_user(int(fname.strip()))
			#udata.location
			locl=udata.location.lower().split()

			if "jammu" in locl:
				pcount+=1	
			if "kashmir" in locl:
				pcount+=1	
			if "j&k" in locl:
				pcount+=1	
			if "akhnoor" in locl:
				pcount+=1
			if "srinagar" in locl:
				pcount+=1
			if "udhampur" in locl:
				pcount+=1
			if "rajouri" in locl:
				pcount+=1
			if "poonch" in locl:
				pcount+=1
			if "baramulla" in locl:
				pcount+=1
			
			if pcount == 0:
				#print "Not found"
				continue
			print str(fname)+" --> found"	
			try:
				fh3.write(str(udata.id)+","+str(udata.screen_name)+","+str(udata.name)+","+str(udata.followers_count)+","+str(udata.statuses_count)+","+str(udata.friends_count)+","+str(udata.favourites_count)+","+str(udata.created_at)+","+str(udata.location)+"\n")	
			except:
				pass
	
		except:
			continue	
			#pass
		
		f=open(fullpath+fname,'r')
		for handle in f:
			handle1=int(handle.strip())
			try:
				if userid[handle1]==0: 
					continue
			except:
				#print "ok"
				userid[handle1]=0
				fh1.write(str(handle1))
				fh1.write("\n")
				#newuserid.append(handle1)
				try:				
					udata = api.get_user(handle1) 
					fd2.write(str(udata.id)+","+str(udata.screen_name)+","+str(udata.name)+","+str(udata.followers_count)+","+str(udata.statuses_count)+","+str(udata.friends_count)+","+str(udata.favourites_count)+","+str(udata.created_at)+","+str(udata.location)+"\n")
					#count=count+1
					#if count>k:
					#	for i in range(InitialLen,len(newuserid)):
					
					#	InitialLen=len(newuserid)
					#	k+=5	
					counter=0
				except tweepy.TweepError as e:
					print e
					try:	
						if e[0][0]['code']==88:	
							counter=counter+1
							if lock==0:
								api = tweepy.API(auth2)
								lock=1
								time.sleep(1)
							elif lock==1:
								api = tweepy.API(auth3)
								lock=2
								time.sleep(1)
							elif lock==2:
								api = tweepy.API(auth4)
								lock=3
								time.sleep(1)
							else:
								api = tweepy.API(auth1)
								lock=0
								time.sleep(1)	
							if counter>3:
								time.sleep(1)
								counter=0
							#time.sleep(361)
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
	#for i in range(InitialLen,len(userid)):
	#	fh1.write(str(userid[i]))
	#	fh1.write("\n")
	#InitialLen=len(userid)
fh1.close()
fd2.close()
fh3.close()
