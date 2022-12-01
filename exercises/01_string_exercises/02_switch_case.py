# Write a Python script to ask for a string, 
# and print the string with uppercase letters in lowercase
# and vice-versa. Include punction and other non-cased 
# characters unchanged.
# E.g.
# Enter a string: Arg!
# aRG!
# Enter a string: PyThoN
# pYtHOn

x=input("Please enter a string ")
print ("The string you entered is :", x)
print ("First capital: ",x.capitalize())
print ("All capital: ",x.upper())
print ("All smallcase: ",x.lower())
print ("Opposite caps: ",x.swapcase())

