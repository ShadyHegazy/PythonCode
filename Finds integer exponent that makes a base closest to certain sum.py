# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 01:02:21 2016

@author: Shady Hegazy
"""
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    def ans(e):
        return base**e
    
    e=0
    while ans(e)<num:
        e+=1
    if ans(e)==num:
        return e
    elif abs(ans(e)-num)>abs(ans(e-1)-num):
        return e-1
    elif abs(ans(e)-num)<abs(ans(e-1)-num):
        return e
    else:
        return e-1