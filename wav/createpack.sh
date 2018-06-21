#!/bin/bash
#drop 9 .wavs into the /wav folder before running this script
echo "Drop 9 wavs in this folder, run this script, those files will be renamed, converted and then created into a pack - the 
original wavs will be deleted from this folder."
sh rename.sh
sh convert.sh
