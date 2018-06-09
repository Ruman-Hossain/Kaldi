import os
def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
#f=open("/home/ruman/kaldi/kaldi/egs/digits/data/test/wav.scp","a")
path="/home/ruman/kaldi/kaldi/egs/digits/digits_audio/train/speaker_1/"
for file in files(path):
	temp=file[:-4]
	out="spearker_1_"+temp+" "+path+""+file
	f=open("/home/ruman/kaldi/kaldi/egs/digits/data/train/wav.scp","a")
	f.write(out+"\n")
	#print(out)
f.close()
