#/usr/bin/python2
#coding: utf-8

import sys, fileinput, os

fo = open("google-images-download.py", "rw+")

line = fo.readlines()[13]
print line

ancien = line
filename = "google-images-download.py"

fo.close()

try:
    keyword = sys.argv[1]
except:
    print 'Merci de saisir des mots clefs pour alimenter la base.'
    sys.exit(1)

nouveau = "search_keyword = ['" + keyword + "']\n"

for line in fileinput.input(filename, inplace=True): 
      print line.replace(ancien, nouveau),


try:
    os.mkdir(keyword) 
    os.chdir(keyword)
    execfile("google-images-download.py")
except OSError:
    pass
