#!/bin/bash
# Modify the paths below for a subset of services.
declare -a services=(
	"/home/badrzahir/lucida/lucida/commandcenter"
	"/home/badrzahir/lucida/lucida/speechrecognition/kaldi_gstreamer_asr"
	"/home/badrzahir/lucida/lucida/imagematching/opencv_imm"
	"/home/badrzahir/lucida/lucida/questionanswering/OpenEphyra"
	"/home/badrzahir/lucida/lucida/calendar"
	"/home/badrzahir/lucida/lucida/djinntonic/dig"
	"/home/badrzahir/lucida/lucida/djinntonic/face"
	"/home/badrzahir/lucida/lucida/djinntonic/imc")

for i in "${services[@]}"
do
   echo "Starting service in $i"
   cd $i
   make start_server
done
