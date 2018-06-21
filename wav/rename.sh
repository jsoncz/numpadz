#!/bin/bash
a=1
for i in *.wav ; do
new=$(printf "%04d.wav" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done
