# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:43:22 2016

@author: Shady Hegazy
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a>b:
        gcdguess=b
    elif b>a:
        gcdguess=a
    else:
        gcd=a
    while gcdguess>=1:
        if (a)%(gcdguess)==0 and (b)%(gcdguess)==0:
            gcd=gcdguess
            break
        else:
            gcdguess-=1
    return gcd