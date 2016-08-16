# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys 
import os

def count():
    dic={}
    #f=open('C:/Users/sx/Desktop/test.txt','w')
    with open(sys.argv[1]) as f:    # use the first parameter as input file
        for line in f:
            line=line.strip()    #delete '\n' at the end of the line
            if line not in dic:
                dic[line]=1
            else:
                dic[line]+=1
# sort by keys:
    file=open(sys.argv[2],'a+')
    for key in sorted(dic.keys()):       # can use iterkeys() or iteritems() if with multiple key/values
        file.write(key + '\t' + str(dic[key]) + '\n')
    file.close()
'''
# sort by values:
    file=open(sys.argv[2],'a+')    # use the second parameter as output file; a+ append to a existing file, or create a new file if it doesn't exit
    for key,value in sorted(dic.items(), key=lambda (k,v): (v,k)):       # lambda: difine one-line mini-functions
        file.write(key + '\t' + str(value) + '\n')
    file.close()
'''
count()