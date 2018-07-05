str="Jammu and Kashmir india J&K Shrinagar"
strl=str.lower().split()

if "jammu" in strl:
	print "     jammu"	
if "kashmir" in strl:
	print "     kashmir"	
if "j&k" in strl:
	print "     j&k"	
if "shrinagar" in strl:
	print "     shri"

for i in strl:
    print i	

