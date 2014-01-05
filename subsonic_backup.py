#!/usr/bin/python
#make backup of subsonic database files

import sys, re, subprocess, shutil, os

#check number of arguments
if len(sys.argv) != 1:
	print "Error! Usage: sudo ./subsonic_backup.py"
else:

	date ='date +%Y%m%d'
	proc= subprocess.Popen([date], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	(save, err) = proc.communicate()
	save = save.strip()

#set directory variables
	dst = '/var/subsonic/db_bkp_' + save
	src = '/var/subsonic/db/'
	
#check and create backup directory
	if not os.path.exists(dst):
		os.makedirs(dst)
	else:
		print "Warning: Directory already exists!"

#get file list of source directory
	flist= os.listdir(src)
	for file in flist:
		infile = os.path.join(src,file)
		shutil.copy(infile, dst)
		print infile.ljust(50), '[DONE]'
	print "complete..."

