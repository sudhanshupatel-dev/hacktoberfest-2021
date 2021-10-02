# Python Program to find Area of an Equilateral Triangle
import math

side = float(input('Please Enter Length of any side of an Equilateral Triangle: '))

# calculate the area
Area = (math.sqrt(3)/ 4)*(side * side)

# calculate the Perimeter
Perimeter = 3 * side

# calculate the semi-perimeter
Semi = Perimeter / 2

# calculate the Altitude
Altitude = (math.sqrt(3)/2)* side

print("\n Area of Equilateral Triangle = %.2f" %Area)
print(" Perimeter of Equilateral Triangle = %.2f" %Perimeter)
print(" Semi Perimeter of Equilateral Triangle = %.2f" %Semi)
print(" Altitude of Equilateral Triangle = %.2f" %Altitude)
