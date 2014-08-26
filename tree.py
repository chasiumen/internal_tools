#!/usr/bin/python


#takes 1 argument path
#print list of files and directies below the path
# ./tree.py PATH


#1. get list  of file/dir and print out
#2. determain if file/dir
#3. output

import sys, os


def ls(path):
    #get list of file/dir on the current dur
    clist  = os.listdir(path)
    #print all path
    for i in clist:
        current_path = os.path.join(path, i)
        #print current_path
        print i
        
        #check dir and run again
        if os.path.isdir(current_path):
            ls(current_path)
        else:
            pass


if len(sys.argv) != 2:
    print "Error! Usage: ./tree.py PATH"

else:
    #check dir path
    if os.path.exists(sys.argv[1]):
        ls(sys.argv[1])
    else:
        print "There is no such a directory", sys.argv[1]

