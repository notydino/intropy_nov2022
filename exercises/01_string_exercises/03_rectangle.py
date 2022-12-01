# Write a Python script to ask for the length and width of a rectangle, 
# calculate and print the perimeter and area of the rectangle.
# E.g.
# Enter length: 5
# Enter width: 3
# perimeter = 16, area = 15.
try:
    x=int(input("Please insert X "))
    y=int(input("Please insert Y "))
except:
    print("Error, please use int only")
else:
    print("The Area is : ", x, " * ", y, "=", f'{x*y:.2f}')
12