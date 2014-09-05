#!/usr/bin/python
#description: This program will rename downlaoded anime files
#version 1.0

#-*- coding: utf-8 -*-
import re, os, sys, shutil


#working dir
path='./'

#Check File access/persmission
def accessCheck(x):
    if os.access(x, os.R_OK):
        print "Read: OK"
    else:
        print "Read: FAIL"
    if os.access(x, os.W_OK):
        print "Write: OK"
    else:
        print "Write: FAIL"
    if os.access(x, os.F_OK):
        print "File: OK"
    else:
        print "File FAIL"
        sys.exit("Error! %s does not exist!!"%(x))


#Get list of file/dir name  path:desired dir
def ls(path):
    return os.listdir(path)

#rename file names
def parseFile(infile):
    x=re.split('\[*\]\s+', infile)
#    print "FileNameList: ", x
    fileName=x[1]
#    print "fileName:", fileName
    return fileName

#Parse dirname
def mkdir(infile):
    x=re.split(ur'\[*\]\s+', infile)
    x=re.split(ur'\s+-\s+', x[1])
    dirName=x[0]
#    print "mkdir_array:", dirName
    return dirName

#Rename
def rename(path, fileNameOri, fileNameDest, dirName):
    #check file access
    src=os.path.join(path, fileNameOri)
    dst=os.path.join(path, dirName, fileNameDest)
    dirNew=os.path.join(path, dirName)
#    print "src: %s" %src
#    print "dst: %s" %dst
    #Check file duplicate
    if os.path.isfile(dst):
        print "Error! %s exists in the destination!" %fileNameDest
        sys.exit()
    else:
        try:
            #Create directory
            os.mkdir(dirNew)
            #move file to dirNew
            shutil.move(src, dst)
            print "%s:       [OK]" %fileNameDest
        except IOError:
            print "Error!", shutil.Error
            sys.exit()
    

############### MAIN ###############
#       //Precondition: Number of Arg
#   1. Get list of file/dir
#   2. Rename

# [] GET_THIS_VALUE  -


#infile = './[Zero-Raws] Seirei Tsukai no Blade Dance - 06 (MBS 1280x720 x264 AAC).mp4'
#access_check(infile)
#Check number of arg
if len(sys.argv) != 1:
    print len(sys.argv)
    sys.exit("Error! Usage: ./rename PATH")
else:
    counter=0
    print "Argument check: [OK]"
    #Get list of files from current dirctory
    infileList = ls(path)
#    print "infile: ", infileList
    #Read each files
    for infile in infileList:
        #print 'debug: ', infile
        if re.search('\[*\]\s+', infile):
#            print "infile: ", infile
            fileName=parseFile(infile)
            dirName=mkdir(infile)
            #rename(fileNameOri, fileNameDest, dirName)
            rename(path, infile, fileName, dirName)
            counter +=1
        else:
            pass
    print "Complete [%d]" %counter
