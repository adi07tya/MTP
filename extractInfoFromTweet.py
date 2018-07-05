import json
fh1=open("/home/pawan/MTech2.2/MTP/MTPCodeData/tweetcorpus_ARFF/adgpi",'r')
data=fh1.readline()
jstr = data[0].replace("'", "\"")
jd=json.loads(jstr)
print type(jd)
