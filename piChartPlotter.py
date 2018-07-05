import matplotlib.pyplot as plt
 
# Data to plot

fh=open("/home/pawan/MTech2.2/MTP/MTPCodeData/TwitterFollowerNetwork/Analysis/monthWiseSentiments_3.txt",'r')
lines=fh.readlines()
line1=lines[0].strip().split(',')
line2=lines[1].strip().split(',')
line3=lines[2].strip().split(',')
labels = 'Negative', 'Neutral', 'Positive'
for i in range(0,14):
	sizes = [line1[i], line2[i], line3[i]]
	colors = ['red', 'gold', 'green']
	explode = (0.1, 0, 0)
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
	plt.axis('equal')
	plt.show()
	break
#colors = ['gold', 'yellowgreen', 'lightcoral'] #, ''
  # explode 1st slice
 
# Plot

