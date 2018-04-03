# This code prints out the numeber of vowels in a given word
NV=0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
       NV+=1
print("Number of vowels: " + str(NV))
