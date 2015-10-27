import sys

#open file for reading
cFile = open(sys.argv[1], "r")


#initialize sequence counter
count=1
seqSize = 0
cSeq=""

#read infile line by line
for line in cFile:
	if(line[0] == ">"):	
		cName=line
		if(count != 1):
			print cSeq.strip()
			cSeq=""
			print cName.strip()
		else:
			print cName.strip()
	else:
		cSeq+=line.strip()
	count+=1

print cSeq.strip()
