# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:03:15 2016

@author: Shady Hegazy
"""
def polysum(n,s):
    """
    Input: n=positive int representing the number of sides of a polygon.
           s=positive int representing the length of each side.
    Returns: Sum= area + square of perimeter
    """
    
    def polygon_area(n,s):
        """
        Input: n=positive int representing the number of sides of a polygon.
               s=positive int representing the length of each side.
        Returns: area of the polygon
        """
        import math
        return (0.25*n*(s**2))/(math.tan((math.pi)/n))
   
    def polygon_perimeter(n,s):
        """
        Input: n=positive int representing the number of sides of a polygon.
               s=positive int representing the length of each side.
        Returns: perimeter of the polygon
        """
        return n*s
    return round(((polygon_area(n,s))+((polygon_perimeter(n,s))**2)), 4)