# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:11:35 2022

@author: cheanshe
"""
#%%
xxx=input("What number am I thinking of? : ")


if xxx:
    try:
        xxx=int(xxx)
    except:
        print("You had one job")
    else:
        print("You guessed ",xxx)
else:
    print("You couldn't even be bothered to write something?")

    
if type(xxx) is int:
    if xxx == 50:
        print("'in a deadpan voice'")
        print("Wow amazing, that was what I was thinking!")
    else:
        print("Good try but bad guess")
else:
    print("You had one job")

-
#%%
squares = [i**2 for i in range(1,11)]
print(squares)





# %% List Comprehension (2)
# 2 ways to get the same results

alist = ['Java', 'Rust', 'Python', 'Swift', 'Go']
filtered_list = [i for i in alist if 'o' in i]
print(filtered_list)

for i in alist:
    if 'o' in i:
        filtered_list.append(i)
    print(filtered_list)

# %% List Comprehension (2)
# 2 ways to get the same results
s = 'Testing 123! Are you there?'
t = [c if c.isalpha() else ' ' for c in s]
u = ''.join(t)
print(u)

#longer way
t=[]
for c in s:
    t.append(c if c.isalpha() else '')
    u = ''.join(t)
print(u)
#%%
fruits = ('apple', 'orange', 'pear')
prices = (1.5, 2.5, 4)
inventory = dict(zip(fruits, prices))

print(inventory)

discounted_inventory = {k: 0.9 * inventory[k] for k in inventory}
print(discounted_inventory)

#%%

#Generator Expression
#This syntax stores a one time use algorithm called a generator
#it stores the equation but not the actual result thus saving memory
#after it's invoked (in a for loop for example), the generate is spent and 
#cannot be invoked again
squares2 = (i**2 for i in range(1,101))

range(0,1000)


#%% Exception handling
# The while loop in this case doesn't have a exit condition, therefore will loop forever
# Thus the loop interrupt will be carried out by breakm
while True:
    try:
    	num = int(input('Enter a number: '))
    except:
        print('Not a number!')
    else:
        print(f'You have entered {num}')
        break
    finally:
    	print('Bye!')