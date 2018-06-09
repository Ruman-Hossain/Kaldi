import os

input_file1 = open("/home/ruman/kaldi-trunk/egs/kobita/data/test/text", "r")
output_file1= open("/home/ruman/kaldi-trunk/egs/kobita/data/local/corpus1", "w") #Temporary Output file for Test Data

input_file2 = open("/home/ruman/kaldi-trunk/egs/kobita/data/train/text", "r")
output_file2= open("/home/ruman/kaldi-trunk/egs/kobita/data/local/corpus2", "w") #Temporary Output file for Test Data

for line in input_file1:
	new_line=line.split(" ")
	#print(new_line)
	length=len(new_line)
	#print(length)
	rslt=""
	for a in range(1,length):
		if a>1:
			rslt+=(" "+new_line[a])
		else:
			rslt+=new_line[a]
	#print(rslt)
	output_file1.write(rslt)
output_file1.close()

for line in input_file2:
	new_line=line.split(" ")
	#print(new_line)
	length=len(new_line)
	#print(length)
	rslt=""
	for a in range(1,length):
		if a>1:
			rslt+=(" "+new_line[a])
		else:
			rslt+=new_line[a]
	#print(rslt)
	output_file2.write(rslt)
output_file2.close()

with open("/home/ruman/kaldi-trunk/egs/kobita/data/local/corpus1","r") as f:
    input1 = f.read()
with open("/home/ruman/kaldi-trunk/egs/kobita/data/local/corpus2","r") as f:
    input2 = f.read()
output = input1+input2 #Final Output File from output_file1 and output_file2 (merged)
with open("/home/ruman/kaldi-trunk/egs/kobita/data/local/corpus.txt", "a") as myfile: 
    myfile.write(output)

os.remove("/home/ruman/kaldi-trunk/egs/kobita/data/local/corpus1")	
os.remove("/home/ruman/kaldi-trunk/egs/kobita/data/local/corpus2")

