# Write a Python script to find the second largest value in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -55, 185]
print(f'{alist=}')

blist=sorted(alist)
clist=sorted(alist, reverse=True)
print(f'{blist=}')
print(f'{clist=}')

print("The 2nd biggest value is ", clist[1])
print("The 2nd biggest is also ", sorted(alist)[-2])
print("The 2nd biggest is definitely ", f"{sorted(alist)[-2]:.2f}")

print(f'{sorted(alist)[-2]:.2f}')
#print(f'{sorted(alist):.2f}')