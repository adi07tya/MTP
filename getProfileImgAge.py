import tweepy
import time
import wget
import os
import random
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
#pawan
#access_token = "355028808-FNqjJhRf0Dzum1bLD7oMhCbTgYjFv7sEDMOPDqqu"
#access_token_secret = "2BZwCGLqYmhttD7j8o7ff2ZEPoQfLVBaqL5TaXZfOoFQh"
#consumer_key = "VA0K4AhozBE0gVw88zS81WLPu"
#consumer_secret = "RtSQs088lMisOwWRjE0L24RJbAHZcRhLPlzTqfSXBVV2ZTKHE3"


#sahil
consumer_key ="0gJKKyXscmsXOfPVdMFu0rD5u"
consumer_secret ="Pof0NF9X5aOGypoz3osdvgOz6Sp7KbReiLRJ4ljsONcIndH34y"
access_token = "1525179444-clyR2Y8hHU0ckeXsm5MzTwFdFKehgLeO40ktxnV"
access_token_secret="4euhYSdGGss1HjyUb9h2WNwi0xt0pwBXikyT9xscR1MXF"




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

path="/home/pawan/MTech2.2/MTP/MTPCodeData/RandomAgeAnalysis/"
folder="Second10000"
userid=[]
if(os.path.exists(path+'AllUsedIDs.txt')):
	f=open(path+'AllUsedIDs.txt', 'r')
	lines = f.readlines()
	userid =[int(e.strip()) for e in lines]
	f.close()


InitialLen=len(userid)

count=0;
k=100



fh1=open(path+'AllUsedIDs.txt', 'a')
fh3=open(path+"adgpi", 'r')
#fh3=open(path+"InitialID_JnK.txt",'r')
lines=fh3.readlines()

file_path_arff=path+folder+'_.arff'
if(not os.path.exists(file_path_arff)):
	fd2=open(file_path_arff, 'a')
	fd2.write("@relation adgpi")
	fd2.write("\n\n@attribute id numeric \n")		
	fd2.write("@attribute userid numeric\n")
	fd2.write("@attribute screen_name string \n")
	fd2.write("@attribute name string\n")
	fd2.write("@attribute followers_count numeric\n")
	fd2.write("@attribute statuses_count numeric\n")
	fd2.write("@attribute friends_count numeric\n")
	#fd2.write("@attribute location string\n")
	fd2.write("@attribute favourites_count numeric\n")
	fd2.write("@attribute location string\n")
	fd2.write("\n@data\n")
	
else :
	fd2=open(file_path_arff, 'a')




while True:
    try:
	line_number=random.randrange(0, len(lines))
	
	user=lines[line_number].strip()
	
	if user in userid: 
		continue
	userid.append(user)		
	udata = api.get_user(user)
	#udata = next(users)
	#fd2.write('{"id":'+str(udata.id).encode('utf-8')+',"screen_name":"'+str(udata.screen_name).encode('utf-8')+'","name":"'+str(udata.name).encode('utf-8')+'","followers_count":'+str(udata.followers_count)+',"statuses_count":'+str(udata.statuses_count)+',"friends_count":'+str(udata.friends_count)+',"favourites_count":'+str(udata.favourites_count)+'}\n')
	fd2.write(str(udata.id)+","+str(udata.screen_name)+","+str(udata.name)+","+str(udata.followers_count)+","+str(udata.statuses_count)+","+str(udata.friends_count)+","+str(udata.favourites_count)+","+str(udata.location)+"\n")
	
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
			fh1.write(str(userid[i]))
			fh1.write("\n")
		InitialLen=len(userid)
		k+=100	
	if count>=12000:
		for i in range(InitialLen,len(userid)):
			fh1.write(str(userid[i]))
			fh1.write("\n")
		InitialLen=len(userid)
		break;
	#print handle	
       # time.sleep(60*15)
    except :
	#print e
	pass
	
	
    #fh.write(str(user).encode('utf-8'))
    #fh.write('\n')	
    #print user.id

fd2.close()


fh1.close()
fh3.close()
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
