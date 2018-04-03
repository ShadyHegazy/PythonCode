# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 06:00:41 2016

@author: Shady Hegazy
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    def create_initial_dict(listA, listB):    
       i=0
       di=[]
       while i<(len(listA)):
           di.append(listA[i]*listB[i])
           i+=1
       return di
    s=0
    di=create_initial_dict(listA, listB)   
    for c in range(len(di)):
        s=s+di[c]
        c+=1
    return s
        
        