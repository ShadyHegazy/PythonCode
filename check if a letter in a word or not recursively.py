# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:14:29 2016

@author: Shady Hegazy
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr)==1:
        return aStr==char
    elif aStr==' ':
        return aStr==char
    elif aStr=='':
        return False
    elif aStr[(len(aStr))//2]==char:
        return True
    elif aStr[(len(aStr))//2]>char:
        return isIn(char, aStr[ 0:((len(aStr))//2)])
    elif char>aStr[(len(aStr))//2]:
        return isIn(char, aStr[((len(aStr))//2):(len(aStr))])
    else:
        return False
       