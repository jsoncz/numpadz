#!/bin/bash
echo "This script requires /usr/share/dict/cracklib-small to generate random pack names"
echo "if you can't get it, you can create a folder with 9 wavs, names 0001.wav to 0002.wav"
echo "and add it manually to packlist.txt to create a pack, results may vary without converting first"
 
a=$(shuf -n1 /usr/share/dict/cracklib-small)
if [ -d "$DIRECTORY" ]; then
  	# Control will enter here if $DIRECTORY exists.
  	a=$(shuf -n1 /usr/share/dict/cracklib-small)
else 
	mkdir ${a}
fi

echo ${a}
for i in *.wav ; do
	  ffmpeg -i $i -ar 22050 ${a}/$i;
done
	
echo "Completed! this pack should automatically be added to the program"
echo $a >> packlist.txt
rm *.wav
