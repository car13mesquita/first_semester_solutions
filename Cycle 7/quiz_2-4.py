# Author CAM (AMDG) 02/23/2020

directions1 = input("Enter 3 cardinal directions: ")
directions2 = input("Enter 3 more cardinal directions: ")

instructions = directions1.split() + directions2.split()

robot_directions = []

if instructions[0] == "north":
    robot_directions.append(1)
elif instructions[0] == "east":
    robot_directions.append(2)
elif instructions[0] == "south":
    robot_directions.append(3)
elif instructions[0] == "west":
    robot_directions.append(4)
else:
    print("The first direction entered is incorrect. The robot will not move.")
    robot_directions.append(0)

if instructions[1] == "north":
    robot_directions.append(1)
elif instructions[1] == "east":
    robot_directions.append(2)
elif instructions[1] == "south":
    robot_directions.append(3)
elif instructions[1] == "west":
    robot_directions.append(4)
else:
    print("The second direction entered is incorrect. The robot will not move.")
    robot_directions.append(0)

if instructions[2] == "north":
    robot_directions.append(1)
elif instructions[2] == "east":
    robot_directions.append(2)
elif instructions[2] == "south":
    robot_directions.append(3)
elif instructions[2] == "west":
    robot_directions.append(4)
else:
    print("The third direction entered is incorrect. The robot will not move.")
    robot_directions.append(0)

if instructions[3] == "north":
    robot_directions.append(1)
elif instructions[3] == "east":
    robot_directions.append(2)
elif instructions[3] == "south":
    robot_directions.append(3)
elif instructions[3] == "west":
    robot_directions.append(4)
else:
    print("The fourth direction entered is incorrect. The robot will not move.")
    robot_directions.append(0)

if instructions[4] == "north":
    robot_directions.append(1)
elif instructions[4] == "east":
    robot_directions.append(2)
elif instructions[4] == "south":
    robot_directions.append(3)
elif instructions[4] == "west":
    robot_directions.append(4)
else:
    print("The fifth direction entered is incorrect. The robot will not move.")
    robot_directions.append(0)

if instructions[5] == "north":
    robot_directions.append(1)
elif instructions[5] == "east":
    robot_directions.append(2)
elif instructions[5] == "south":
    robot_directions.append(3)
elif instructions[5] == "west":
    robot_directions.append(4)
else:
    print("The sixth direction entered is incorrect. The robot will not move.")
    robot_directions.append(0)

print("In order to have the robot move {0}, give it this sequence, {1}.".format(instructions, robot_directions))
