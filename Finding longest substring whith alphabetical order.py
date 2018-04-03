#prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then the program will print "Longest substring in alphabetical order is: beggh"
#In the case of ties, prints the first substring. For example, if s = 'abcbcd', then the program will print "Longest substring in alphabetical order is: abc"

# initialise tracker variables
maxLen=0
current=s[0]
longest=s[0]

# step through s indices
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        current += s[i + 1]
        # if current length is bigger update
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
    else:
        current=s[i + 1]
        
    i += 1

print ('Longest substring in alphabetical order is: ' + longest)
