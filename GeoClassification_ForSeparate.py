import sys
import os
path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"
#fname=str(sys.argv[1])+"_.arff"
fname="separate.txt"
userid={}
if(os.path.exists(path+"Analysis/JnK_TwitterUsersIDs.txt")):
	f=open(path+"Analysis/JnK_TwitterUsersIDs.txt", 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()



#path="/home/pawan/MTech2.2/MTP/MTPCodeData/Try/eg1.txt"
fd=open(path+fname,'r')
#fd=open('D:/adish/iitg/MTP/WEKA/OtherArmies/britisharmy_arff.arff','r')
count = 1
fcount=0
ids=[]
rtcount=[]
fromJnK=0
total=0
numGeoTagged=0


#rtcount2=[]
while True:
    data=fd.readline()
    #if count<=14:
    #    count+=1
      #  continue
    if data == '':
        break
    else:
        total+=1
        list=data.split(",")
	try:
		if userid[int(list[0])]==0:
			continue
	except:
		if len(list)>8:
			
			locl=[]
			pcount=0
			#print len(list) 
			#print len(str(list[8]))
			if len(list)==9 and len(str(list[8]))<2:
				continue
			numGeoTagged+=1
			for i in range(8,len(list)):
				locl.extend(list[i].lower().strip().split())
			#str1=""	
			#for j in locl:
			#	str1+=str(j)+" "
			#print str1	
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
			if pcount>0:
				fromJnK+=1
			if pcount==0:
				str1=""	
				for j in locl:
					str1+=str(j)+" "
				print str1		
print fname
print "Total : "+str(total)
print "Geo Tagged : "+str(numGeoTagged)
print "fromJnK : "+str(fromJnK)

       

'''
print "Total tweet ="+str(count-17)
print "False retweeted count = "+str(fcount)
#print "Retweeted = "+str(str(count-17)- str(fcount))
'''
