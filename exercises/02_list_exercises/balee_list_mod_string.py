# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:05:26 2022

@author: cheanshe
"""

astring = "Testing 1234!"

alist = list(astring)

blist = []
for i in alist:
    if i.isalpha():
        blist.append(i)

print(astring)
print(alist)
print(blist)
print(''.join(blist))
print('*'.join(blist))

#https://unicode.party/
print("😒")



xxx=("the quick brown fox jumps over the lazy dog")

print(xxx)
print(sorted(set(xxx)))
print("Total number of unique characters are ",len(sorted(set(xxx))))

import re 
astring = 'The quick brown fox jumps over the Lazy dog. ' 
bstring=re.sub(r'[ \W_]', '',astring) 
print ("The sentence is ",astring) 
print( "This sentence consist of these alphabets : ", ''.join(set(bstring.lower()))) 
print( "Which can be sorted as :", ''.join(sorted(set(bstring.lower())))) 

