# Author CAM (AMDG) 02/23/2020

sentiment = input("How are you feeling?: ")

if sentiment[:3] != "not":
    sentiment = "not " + sentiment

print("You're {0}. Now SCRAM!".format(sentiment))
