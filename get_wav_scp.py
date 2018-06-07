import os

data_path = "/home/ruman/kaldi/kaldi/egs/digits/digits_audio/train"

sp_list = os.listdir(data_path)
sp_list.sort()
wsp = ""
for sp in sp_list:
	sp_path = data_path + "/" + sp
	wav_list = os.listdir(sp_path)
	wav_list.sort()
	for wav in wav_list:
		wav_path = sp_path + "/" + wav
		wsp = wsp + sp + "_" + wav[:-4] + " " + wav_path + "\n"

file = open("/home/ruman/kaldi/kaldi/egs/digits/data/train/wav.scp","w")
file.write(wsp)
file.close()

#To sort the file now run from terminal on the containing directory :$  sort -k 1,1 wav.scp