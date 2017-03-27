#!/bin/bash
mongo lucida<<EOF

function Populate
{
   local dossierCourant=$1
   for image in $dossierCourant/*
    do
	echo $(basename $image)
	echo $(dirname $image)
	db.images_zahir.insert({'image_id':$(basename $image),'data': $(basename $image),'label': $(dirname $image)})
   done
}
 
[ $1 ] && {
   Populate $1
} 
quit()
EOF
