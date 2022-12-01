# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

alist = [c.lower() for c in astring if c.isalpha()]
print(alist)

#solution 1
d1 = {}
for i in sorted(set(alist)):
    d1[i] = alist.count(i)
print(d1)


#%% solution 2
d2 = {c: alist.count(c) for c in sorted(set(alist))}
print(d2)

for k in d2:
    print(f"{k} appears {d2[k]} {'times' if d2[k] > 1 else 'time'}")