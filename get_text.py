input_file = open("/home/ruman/kaldi/kaldi/egs/digits/data/test/wav.scp", "r")
output_file= open("text", "w")

dic = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", 
		"5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}

for line in input_file:
	print(line)
	line= line.strip("\n")
	new_line=line.split(" ")
	output_file.write(new_line[0] + " ")
	#print(new_line[0] + " ")
	line_split=new_line[0].split("_")
	fname= line_split[len(line_split)-1]
	##fname.strip('\n')
	if len(fname)==3 and fname[0]==fname[1]:
		output_file.write("double " + dic[fname[0]])
		#print("double "+dic[fname[0]])
	else:
		for l in range(0, len(fname)):
			output_file.write(dic[fname[l]] + " ")
			#print(dic[fname[l]] + " ")
	output_file.write("\n")