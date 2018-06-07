import glob
a=open("path", "w")
for path in glob.glob("/home/ruman/kaldi/kaldi/egs/digits/digits_audio/train/speaker_2/*"):
	temp_path = path.split('.')
	new_path = temp_path[0].split('/')
	fname = new_path[len(new_path)- 1]
	sname = new_path[len(new_path)-2]
	vname = sname + "_" + fname + " "
	# a.write(vname)
	# a.write(path)
	# a.write('\n')
	printf(vname+" " path)
