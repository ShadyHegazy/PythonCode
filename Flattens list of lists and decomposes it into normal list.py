# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 06:59:32 2016

@author: Shady Hegazy
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    new=[] 
    global new
    def internal(aList):
        for i in range(len(aList)):
          if type(aList[i])!=(list):
              new.append(aList[i])
          else:
              internal(aList[i])
        return new
    return internal(aList)
aList=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
