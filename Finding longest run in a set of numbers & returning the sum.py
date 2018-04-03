# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 23:38:25 2016

@author: Shady Hegazy
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    sorter=L[:]
    def incrun(L):
        inrun=[]
        i=0
        n=0
        while i<len(L):
            if n+2>=len(L):
                break
            templist=[]
            done=False
            for n in range(n,len(L)-1):
                if L[n+1]>=L[n]:
                    if not done:
                        templist.append(L[n])
                        templist.append(L[n+1])
                        done=True
                    elif done:
                        templist.append(L[n+1])
                        if n+2==len(L):
                            inrun.append(templist)
                            break
                elif L[n+1]<L[n]:
                    if done:
                        inrun.append(templist)
                        i+=1
                        break
                    elif not done:
                        n+=1
        return inrun

    def decrun(L):
        decrun=[]
        i=0
        n=0
        while i<len(L):
            if n+2>=len(L):
                break
            templist=[]
            done=False
            for n in range(n,len(L)-1):
                if L[n+1]<=L[n]:
                    if not done:
                        templist.append(L[n])
                        templist.append(L[n+1])
                        done=True
                    elif done:
                        templist.append(L[n+1])
                        if n+2==len(L):
                            decrun.append(templist)
                            break
                elif L[n+1]>L[n]:
                    if done:
                        decrun.append(templist)
                        i+=1
                        break
                    elif not done:
                        n+=1
        return decrun
    
    runs=incrun(L)+decrun(L)
    def mergeSort(L):
        if len(L) < 2:
            return L[:]
        else:
            middle = int(len(L)/2)
            left = mergeSort(L[:middle])
            right = mergeSort(L[middle:])
            return merge(left, right)

    def merge(left, right):
        result = []
        i,j = 0, 0
        while i < len(left) and j < len(right):
            if len(left[i])<len(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while (i < len(left)):
            result.append(left[i])
            i += 1
        while (j < len(right)):
            result.append(right[j])
            j += 1
        return result
    runs=mergeSort(runs)
    
    def indexsum(r,sorter):
        x=0
        for char in r:
            x=x+sorter.index(char)
        return x
            
    
    def long_one(runs,sorter):
        if len(runs)<1:
            return None
        elif len(runs)==1:
            return runs
        else:
            lenlist=[]
            indlist=[]
            used=runs[:]
            for l in runs:
                lenlist.append(len(l))
            s=max(lenlist)  
            for l in runs:
                if len(l)<s:
                    used.remove(l)
                else:
                    indlist.append(indexsum(l,sorter))
            if len(indlist)>1:
                result=used[indlist.index(min(indlist))]
                return result
            else:
                result=runs[lenlist.index(max(lenlist))]
                return result
    result=long_one(runs,sorter)
    if result==None:
        return None
    elif type(result[0])==int:
        return sum(result)
    else:
        return sum(result[0])
