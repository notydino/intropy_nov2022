# Write a Python script to find common items between two lists.
alist = [99, 'P', 1, 'xyz', 'a', 2.5]
blist = ['xyz', 2.5, 2.5, 3, 99, 99, 2.5, 'xyz', -1.2, 99]

aset=set(alist)
bset=set(blist)

print("intersection ", aset & bset)
print("union ",aset | bset)
print("diff ", aset - bset)

#%% Alternative solution

clist=[]
for i in alist:
    if i in blist:
        clist.append(i)
print(clist)

#%% List Comprehension method

# Write a Python script to find common items between two lists.
alist = [99, 'P', 1, 'xyz', 'a', 2.5]
blist = ['xyz', 2.5, 2.5, 3, 99, 99, 2.5, 'xyz', -1.2, 99]

dlist=[i for i in alist if i in blist]
print(dlist)
