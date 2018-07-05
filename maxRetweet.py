
#fd=open('/home/pawan/MTech2.2/MTP/MTPCodeData/Try/AK7CAV_arff.arff','r')
fd=open('D:/adish/iitg/MTP/WEKA/OtherArmies/britisharmy_arff.arff','r')
count = 1
fcount=0
ids=[]
rtcount=[]
#rtcount2=[]
while True:
    data=fd.readline()
    if count<17:
        count+=1
        continue
    if data == '':
        break
    else:
        count+=1
        list=data.split(",")
        if str(list[10]) != '0':
                fcount+=1
                ids.append(list[0])
                rtcount.append(int(list[10]))



for i in range(1,len(rtcount)):
    temp1= rtcount[i]
    temp2=ids[i]
    #k=0
    k=i
    for j in range(i-1,-1,-1):
        k=j
        if temp1<rtcount[j]:
            rtcount[j+1]=rtcount[j]
            ids[j+1]=ids[j]
            if j == 0:
                k=-1
	else:
	    break	
    rtcount[k+1] = temp1
    ids[k+1] = temp2
 		
    
for i in range(0,len(ids)):
    print str(ids[i])+"   "+str(rtcount[i])
'''
print "Total tweet ="+str(count-17)
print "False retweeted count = "+str(fcount)
#print "Retweeted = "+str(str(count-17)- str(fcount))
'''
