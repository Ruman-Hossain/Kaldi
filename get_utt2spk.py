input_file = open("/home/ruman/kaldi-trunk/egs/kobita/data/train/wav.scp", "r")
output_file= open("/home/ruman/kaldi-trunk/egs/kobita/data/train/spk2utt", "w")


for line in input_file:
	line= line.split(".")
	#line split by . out like: ['speaker_10_00 /home/ruman/kaldi/kaldi/egs/digits/digits_audio/train/speaker_10/00', 'wav\n']
	#print(line)
	line_without_extinsion= line[0].split("/")
	#Line without extension split by / then output like: ['speaker_10_00 ', 'home', 'ruman', 'kaldi', 'kaldi', 'egs', 'digits', 'digits_audio', 'train', 'speaker_10', '00']
	#print(line_without_extinsion)
	sid= line_without_extinsion[len(line_without_extinsion)-2]
	#sid Speaker ID
	#print(sid)
	fname= line_without_extinsion[len(line_without_extinsion)-1]
	#print(fname)
	################OUTPUT FOR utt2spk ###########################
	#output_file.write(sid + "_"+ fname+ " "+ sid + "\n")

	###############OUTPUT FOR  spk2utt  ###########################
	output_file.write(sid + " "+sid + "_"+ fname + "\n")
	#break #Break used to see the output of one line