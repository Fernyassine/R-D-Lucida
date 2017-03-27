#! /bin/sh 
mongo lucida <<EOF
db.images_zahir.insert({'image_id':'image_cheval_01','data': './Desktop/cheval.jpeg','label': 'cheval'})
quit()
EOF
