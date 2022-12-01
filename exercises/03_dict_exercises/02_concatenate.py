# Write a Python script to concatenate following dictionaries to create a new one.
# Expected Result: 
# d4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
from copy import deepcopy
d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}
d3 = {'e': 50}


dconc=deepcopy(d3)
for d in (d1, d2, d3):
    dconc.update(d)
print(dconc)

#%% using dict comprehsion

dconc={k: d[k] for d in (d1,d2,d3) for k in d}
print(dconc)

#%%

mylist=[]

for i in range (1,4):
    xxx="d"+str(i)
    mylist.append(xxx)
print(mylist)

dconc=deepcopy(d3)
for d in (mylist):
    dconc.update(eval(d))
print(dconc)