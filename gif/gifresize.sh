#!/bin/bash
for i in *.gif ; do
convert -resize 320X240 $i $i
done
