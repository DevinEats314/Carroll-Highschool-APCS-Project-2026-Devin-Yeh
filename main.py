#Devin Yeh APCS project 2026 CHS CISD
import math
e = 2.718281828
pi = 3.1415926525897932384626433 #some constants for functions like e^x
x = 0

func = input("What function to integrate (write as you would in python): ")
def f(x):
    return eval(func)
uselistordx = input("Would you like to use even intervals or a custom list of points? I/L: ") #User settings
if uselistordx == "I":
    dx = float(input("What is your interval (smaller = more accurate): "))
    a = float(input("Lower bound (if negative inf put -100): "))
    b = float(input("Upper bound (if inf put 100): "))
    pointslist = []
    for i in range(int(round((b-a)/dx))):
        pointslist.append(a + i*dx)
elif uselistordx == "L":
    pointslist = []
    for x in input("Input your points separated by commas (no spaces and in order least to greatest): ").split(","):
        pointslist.append(float(x))
    a = pointslist[0]
    b = pointslist[len(pointslist) - 1]
else:
    print("Defaulted to even intervals")
    a = float(input("Lower bound (if negative inf put -100): "))
    b = float(input("Upper bound (if inf put 100): "))
    dx = float(input("What is your interval (smaller = more accurate): "))
    pointslist = []
    for i in range(int(round((b-a)/dx))):
        pointslist.append(a + i*dx)

#integration function here
def approxIntegral(points, func):
    total = 0
    if len(points) < 2:
        return 0 #rectangle of width 0 has area 0 (do more than 2 points)
    for i in range(len(points) - 1):
        x = points[i] #move to the next rectangle
        total += func(x) * (points[i+1] - points[i]) #adds one rectangle width dx length f(x)
    return total

print("")
print("The integral of ", func, " from ", a, " to ", b, " is approximately ", round(approxIntegral(pointslist, f), 3))
