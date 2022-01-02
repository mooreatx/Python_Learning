# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:45:17 2020

@author: moore
"""
import re

file = open('stats.txt', 'r')
contents = file.read()
conSplit = contents.split(',')

def sorter(netinfo):
    
    infoDict = {}
    
    devSwitch = 'switch'
    
    devMatch = re.compile(r'\switch..')
    
    for line in netinfo:
        match = devMatch.finditer(line)
        if match:
            infoDict[line] = 'value'
            

            
    print(infoDict)
    



sorter(conSplit)