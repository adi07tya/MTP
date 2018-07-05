import os
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

monthwise=[]
w,h=14,3   # 0-- neg 1--neu 2 positive
monthwise = [[0 for y in range(w)] for x in range(h)] 


total=0
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
				total+=1
				datalist=data.split(",")
				sentence=str(datalist[1])
				date=str(datalist[2]).split()
				date=str(date[0]).split('-')
				sentiment = analyzer.polarity_scores(sentence)
					
				if sentiment['neg']> 0.5:#{'neg': 0.0, 'neu': 0.254,'pos':0.746,'compound':0.8316}
					sid=0	
				if sentiment['neu']>= 0.5:
					sid=1
				if sentiment['pos']>= 0.5:								
					sid=2						
				if int(date[0])==2016:
					monthwise[sid][int(date[1])-1]+=1
				if int(date[0])==2017:
					monthwise[sid][12+int(date[1])-1]+=1
				#print "2017"
	except:	
		print 	sys.exc_info()[0]
		pass	
fh=open(path+"Analysis/monthWiseSentiments_3.txt",'w')
for i in range(h):
	fh.write(str(monthwise[i][0]))
	for j in range(1,w):
		fh.write(","+str(monthwise[i][j]))
	fh.write("\n")
fh.close()	

print total

print monthwise		
