# Author: CAM (AMDG)  10/14/2021

x1 = int(input("Enter the first x-coordinate: "))
y1 = int(input("Enter the first y-coordinate: "))
x2 = int(input("Enter the second x-coordinate: "))
y2 = int(input("Enter the second y-coordinate: "))

distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2))**(1/2)

print("The distance between the two points is " + str(distance))
