# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

sum_of=0
for i in alist:
    sum_of += i
print(sum_of)

#%%
prod_of=1
for i in alist:
    prod_of *= i
    print(prod_of)
    
#%%

from functools import reduce

reduce(lambda, x, ) #incomplete