import sys
import os
path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"
#folder="OmarObdulah/OA_ARFF"

folder="FollowerARFF"
#folder="separate"

#fname=str(sys.argv[1])+"_.arff"
#path="/home/pawan/MTech2.2/MTP/MTPCodeData/Try/eg1.txt"
#fd=open('D:/adish/iitg/MTP/WEKA/OtherArmies/britisharmy_arff.arff','r')

#fd=open(path+fname,'r')
#count = 1
#fcount=0

fromJnK=0
total=0
numGeoTagged=0


userid={}
doneARFF={}
if(os.path.exists(path+"Analysis/JnK_TwitterUsersIDs.txt")):
	f=open(path+"Analysis/JnK_TwitterUsersIDs.txt", 'r')
	lines = f.readlines()
	for e in lines:	
		userid[int(e.strip())]=0
	f.close()

if(os.path.exists(path+"Analysis/DoneARFFFiles.txt")):
	f=open(path+"Analysis/DoneARFFFiles.txt", 'r')
	lines = f.readlines()
	for e in lines:	
		doneARFF[str(e.strip())]=0
	f.close()


fha1=open(path+"Analysis/JnK_TwitterUsersIDs.txt",'a')


file_path_arff=path+"Analysis/JnK_TwitterUsersData.txt"
if(not os.path.exists(file_path_arff)):
	fha2=open(file_path_arff, 'a')
	fha2.write("@relation JnK")
	fha2.write("\n\n@attribute id numeric \n")		
	fha2.write("@attribute screen_name string \n")
	fha2.write("@attribute name string\n")
	fha2.write("@attribute followers_count numeric\n")
	fha2.write("@attribute statuses_count numeric\n")
	fha2.write("@attribute friends_count numeric\n")
	#fha2.write("@attribute location string\n")
	fha2.write("@attribute favourites_count numeric\n")
	fha2.write("@attribute created_at string\n")
	fha2.write("@attribute location string\n")
	fha2.write("\n@data\n")
else:
	fha2=open(path+"Analysis/JnK_TwitterUsersData.txt",'a')	

fha3=open(path+"Analysis/DoneARFFFiles.txt",'a')

total=0
numGeoTagged=0
fromJnK=0

if(os.path.exists(path+"Analysis/summaryNext.txt")):
	f=open(path+"Analysis/summaryNext.txt", 'r')
	lines = f.readlines()
	sdata=[]
	fhw1=open(path+"Analysis/summaryPrev.txt",'w')	
	for e in lines:
		fhw1.write(e)	
		t=e.strip().split()
		sdata.append(int(t[1]))
	total=sdata[0]	
	numGeoTagged=sdata[1]
	fromJnK=sdata[2]
	fhw1.close()
	f.close()

fullpath=path+folder+"/"
for fname in os.listdir(fullpath):
		
	try:
		if doneARFF[str(fname.strip())]==0:
			continue
	except:
		#print fname
		if str(fname.strip())!="separate.txt":
			doneARFF[str(fname.strip())]=0
			fha3.write(str(fname.strip())+"\n")
		fd=open(fullpath+fname,'r')
		count=0
		while True:
		    data=fd.readline()
		    count+=1 	
		    if count<=14 and str(fname.strip())!="separate.txt":
			continue
		    if data == '':
			break
		    else:
			
			list=data.split(",")
			total+=1
			if len(list)==9 and len(str(list[8]))<2:
					continue
			try:
				if userid[int(list[0])]==0:
						total-=1
						continue
			except:	
				#userid[int(list[0])]=0
				locl=[]
				pcount=0
				numGeoTagged+=1
				for i in range(8,len(list)):
					locl.extend(list[i].lower().strip().split())
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
					fha1.write(str(list[0])+"\n")
					fha2.write(data)
					userid[int(list[0])]=0	

fha1.close()
fha2.close()
fha3.close()

fw=open(path+"Analysis/summaryNext.txt",'w')
fw.write("Total "+str(total)+"\n")
fw.write("GeoTagged "+str(numGeoTagged)+"\n")
fw.write("fromJnK "+str(fromJnK)+"\n")
fw.close()		
				
#print fname
print "Total : "+str(total)
print "Geo Tagged : "+str(numGeoTagged)
print "fromJnK : "+str(fromJnK)

       

'''
print "Total tweet ="+str(count-17)
print "False retweeted count = "+str(fcount)
#print "Retweeted = "+str(str(count-17)- str(fcount))
'''
