import sys

#open file for reading
cFile = open(sys.argv[1], "r")


#initialize sequence counter
count=1
seqSize = 0
cSeq=""
names = [] #storage for names
size = [] #storage for sequence lengths
seq = []

#read infile line by line
for line in cFile:
    if(line[0] == ">"): #is current line a header?
        cName=line #save header
        if(count != 1): #is this the first line in the file?
            size.append(len(cSeq.strip())) #store the size of sequence
            seq.append(cSeq.strip())
            cSeq="" #reset sequence
            names.append(cName.strip()) #store header
        else:
            names.append(cName.strip()) #only store header
    else:
        cSeq+=line.strip() #append sequence
        count+=1 #increment counter

size.append(len(cSeq.strip())) #grab the last very last sequence
seq.append(cSeq.strip())

maxInd = seq.index(max(seq))
print names[maxInd]
print seq[maxInd]

