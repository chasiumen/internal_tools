#!/usr/bin/python
#Description: Remove old backup files
#Date Nov.24 2013
#Author: Ryosuke Morino

import re, sys, subprocess, os, shutil

#set directory variables
src = '/var/subsonic/'
	

#check number of arguments
if len(sys.argv) != 1:
	print "Error! Usage: sudo ./subsonic_backup_remove.py"
else:

	print "Automatic deletion process starts..."


#generate possible directory dates
	# range(	starting day, 		end date,		increment	)
	#			untill 10days ago,	from X day,		1	(static)
	#			1<x<y				, 	x<y,		1
	for x in range(1, 15, 1):
		date ='date +%Y%m%d --date \"' + str(x) +  ' days ago\"'
		#date ='date +%Y%m%d --date \"' + str(x) +  ' days\"'

		proc = subprocess.Popen([date], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		(save, err) = proc.communicate()
		save = save.strip()
		path = src + 'db_bkp_' + save
        print path
		
	#get directory list
		dlist = os.listdir(src)
		for dir in dlist:
			dir = os.path.join(src, dir)

			#check if backup directory exists
			if dir != path:
				pass
			else:
				#print path + ":" + dir.ljust(50), "[MATCH]"
				#delete cmd
				shutil.rmtree(path)
				print path.ljust(50), "[DELETE]"
	print "compelte..."
