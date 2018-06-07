input_file = open("/home/ruman/kaldi/kaldi/egs/digits/data/test/wav.scp", "r")
output_file= open("/home/ruman/kaldi/kaldi/egs/digits/data/test/utt2psk", "w")


for line in input_file:
	line= line.split(".")
	line_without_extinsion= line[0].split("/")
	sid= line_without_extinsion[len(line_without_extinsion)-2]
	fname= line_without_extinsion[len(line_without_extinsion)-1]
	output_file.write(sid + "_"+ fname+ " "+ sid + "\n")