# CAM (AMDG) 11/24/19

weight = int(input("Enter weight in pounds: "))
height = int(input("Enter height in inches: "))

bmi = (703 * weight) / (height ** 2)

if bmi < 19:
    print("You are underweight.")
elif bmi < 25:
    print("You are healthy.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 40:
    print("You are obese.")
else:
    print("You are extremely obese.")
