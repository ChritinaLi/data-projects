# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:33:37 2016

@author: Christina
"""
import sys 
import csv
#from __future__ import division

def density():
    dic={}
    dic_count={}
    lines = []
    total_num = 0
    with open(sys.argv[1]) as file:
        f = csv.reader(file, delimiter = ',',  quotechar = '"')
        for line in f:
            total_num += 1   # count line number in a file
            lines.append(line)
    total_num = total_num - 1
    label_list = lines[0]
    for i in range(0,len(label_list)):
        dic[label_list[i]] = []
        for j in lines[1:]:
            if j[i] != "":
                dic[label_list[i]].append(j[i])
    for i in dic:
        dic_count[i] = round(len(dic[i])/float(total_num),2)

    file=open(sys.argv[2],'a+')
    for key in dic_count:       # can use iterkeys() or iteritems() if with multiple key/values
        file.write(key + ',' + str(dic_count[key]) + '\n')
    file.close()    

density()        
