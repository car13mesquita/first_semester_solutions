# Author: CAM (AMDG) 9/26/2020

radius = input("What is the radius of the cylinder? ")
height = input("What is the height of the cylinder? ")

volume = 3.14 * int(radius) ** 2 * int(height)

surface_area = 2 * 3.14 * int(radius) * (int(height) + int(radius))

print("The volume of the cylinder is: " + str(volume))
print("The surface area of the cylinder is: " + str(surface_area))
