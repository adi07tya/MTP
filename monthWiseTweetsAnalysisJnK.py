import os
import sys

monthwise=[]
w,h=31,14
monthwise = [[0 for y in range(w)] for x in range(h)] 

path="/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/"
folder="JnKTwitterCorpus/"
fullpath=path+folder
for fname in os.listdir(fullpath):
	flist=fname.split('.')
	if len(flist)==1:
		continue
	try:
		if len(flist)==2 and str(flist[1])=='arff':
			fd=open(fullpath+fname,'r')
			count=0
			while True:
			    data=fd.readline()
			    count+=1 	
			    if count<=16:
				continue
			    if data == '':
				break
			    else:
				#print data
				datalist=data.split(",")
				date=str(datalist[2]).split()
				date=str(date[0]).split('-')
				if int(date[0])==2016:
					monthwise[int(date[1])-1][int(date[2])-1]+=1
			
				if int(date[0])==2017:
					monthwise[12+int(date[1])-1][int(date[2])-1]+=1

	except:
		pass	
fh=open(path+"Analysis/monthWiseRecord_2.txt",'w')
for i in range(14):
	fh.write(str(monthwise[i][0]))
	for j in range(1,31):
		fh.write(","+str(monthwise[i][j]))
	fh.write("\n")
fh.close()	

print monthwise		
