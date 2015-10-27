import sys

#open file for reading
cFile = open(sys.argv[1], "r")


#initialize sequence counter
count=1
seqSize = 0
cSeq=""
names = [] #storage for names
size = [] #storage for sequence lengths

#read infile line by line
for line in cFile:
    if(line[0] == ">"): #is current line a header?
        cName=line #save header
        if(count != 1): #is this the first line in the file?
            size.append(len(cSeq.strip())) #store the size of sequence
            cSeq="" #reset sequence
            names.append(cName.strip()[1:]) #store header
        else:
            names.append(cName.strip()[1:]) #only store header
    else:
        cSeq+=line.strip() #append sequence
        count+=1 #increment counter
size.append(len(cSeq.strip())) #grab the last very last sequence

#print output
out = "\n".join( "\t".join(map(str,i)) for i in zip(names, size) )
print "seqName\tseqLength"
print out
