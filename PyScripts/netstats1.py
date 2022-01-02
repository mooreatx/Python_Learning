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
    
    devPat = 'switch..'
    intPat = 'te...'
    bpsPat = r'\b[0-9]\d+\b'
    
    devMatch = re.findall(devPat, netinfo)
    intMatch = re.findall(intPat, netinfo)
    bpsMatch = re.findall(bpsPat, netinfo)
    
    #print(devMatch)
    #print(intMatch)
    #print(bpsMatch)
    
    for dev, int, bps in zip(devMatch, intMatch, bpsMatch):
        infoDict['{}--{}'.format(dev, int)] = bps

    newDict = dict(zip(infoDict.keys(), [float(value) for value in infoDict.values()]))
	
    
    for k,v in sorted(newDict.items(), key=lambda x:x[1]):
        print(k, v)

sorter(contents)
