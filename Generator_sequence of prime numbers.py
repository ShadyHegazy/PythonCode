# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:21:21 2016

@author: Shady Hegazy
"""

def genPrimes():
    global conca
    global num
    conca=[2]
    num=2
    
    if num==2:
        num+=1
        yield conca[-1]      
    while num>2:
        j=0
        for n in conca:
            if num%n!=0:
                j+=1
            else:
                break
        if j==len(conca):
            conca.append(num)
            num+=1
            yield conca[-1]
        else:
            num+=1

    
    
    