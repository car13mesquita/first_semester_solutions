# Author: CAM (AMDG)  10/14/2021

p = float(input("Enter investment amount: "))
r = float(input("Enter the annual interest rate as a percent: "))
t = int(input("Enter the time the investment will rest in the account: "))

n = 12
r /= 100

future_value = p * ((1 + (r / n)) ** (n * t))

print("In " + str(t) + " years, the account will contain $" + str(future_value))

