# THIS CODE IS NOT SO USEFUL, BUT IT REQUIRES SKILLFUL PLAYING WITH DATA SETS.
#I created it just to help my little brother solve his homework

def get(allsum, length):
    '''
    input: allsum: the sum of all digits in a number.
           length: the number of digits that the number consists of.
    output: the largest number that consists of a number of UNIQUE digits that is equal 
            to length, and their sum is equal to all sum.
    Example: get(35, 7) 9876410 which is the largest number that consists of 7 DIFFERENT digits
             whose sum is 35.
    '''
    basics=[9,8,7,6,5,4,3,2,1,0]
    rebasics=[0,1,2,3,4,5,6,7,8,9]
    upperlimit=sum(basics[0:length])
    lowerlimit=sum(basics[(10-length):10])
    
    def glue(list):
        s=''
        for j in range(len(list)):
            s=s+str(list[j])
            j+=1
        return s
    def final(sliced,h):
        g=len(sliced)-1
        v=0
        global slicedclone
        slicedclone=sliced[:]
        if (sum(slicedclone)-h)==0 and AllDifferent(slicedclone)==True:
            return slicedclone
        elif (sum(slicedclone)-h)!=0:
            while g>=0 and (sum(slicedclone)-h)!=0:
                 if slicedclone[g]==rebasics[v]:
                     v+=1
                     g-=1
                 else:
                     slicedclone[g]-=1
            return slicedclone
                     
        
    def getslice(sliced):
        k=sum(initial[0:q+1])-sum(initial[0:q])
        if k==0:
            return initial
        else:
            return final(sliced,h)
            
    def AllDifferent(s):
       for i in range(len(s)):
           for i2 in range(len(s)):
               if i != i2:
                   if s[i] == s[i2]:
                       return False
       return True
    
    if allsum>upperlimit or allsum<lowerlimit :
        print('Impossible!!!')
        return None
    initial=basics[0:length]
    for q in range(len(initial)):
        if (sum(initial[0:q+1])-allsum)<0:
            q+=1
        elif (sum(initial[0:q+1])-allsum)>=0:
            sliced=initial[q:len(initial)]
            break
    h=allsum-sum(initial[0:q]) 
    slicedclone=getslice(sliced)
    result=initial[0:q]
    result.append(slicedclone)
    end=glue(initial[0:q])+glue(slicedclone)
    print(end+' is the larget number that consists of '+str(length)+' UNIQUE digits whose sum is '+str(allsum))
length=int(input('Enter the number of digits :  '))
allsum=int(input('Enter the sum of the digits:  '))
get(allsum, length)