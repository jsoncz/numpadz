#!/bin/bash
for i in *.wav ; do
	  ffmpeg -i $i -ar 22050 threaten/$i
done
	