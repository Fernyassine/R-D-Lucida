#/usr/bin/python2
#coding: utf-8

import sys, fileinput, os

fo = open("/home/badrzahir/lucida/Lucida-populate-db/google-images-download.py", "rw+")

line = fo.readlines()[13]
print line

ancien = line
filename = "/home/badrzahir/lucida/Lucida-populate-db/google-images-download.py"

fo.close()

try:
    keyword = sys.argv[1]
    print keyword
    print '$$$$$$$$$$$$'
except:
    print 'Merci de saisir des mots clefs pour alimenter la base.'
   # sys.exit(1)

nouveau = "search_keyword = ['" + keyword + "']\n"

for line in fileinput.input(filename, inplace=True): 
      print line.replace(ancien, nouveau),


try:
    os.mkdir("/home/badrzahir/Desktop/"+keyword) 
    os.chdir("/home/badrzahir/Desktop/"+keyword)
    execfile(filename)
except OSError:
    pass
