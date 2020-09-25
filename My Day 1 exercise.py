print(1 + 2)
print(3.4 + 11)
print(8 + 4.0)
print("7-5=" + str(7-5))
print("-6.0 + 11.78 = " + str(-6.0 + 11.78))
#calculate and print age
print("\n calculate your age")
#print("My age: " + input("What is your age?"))

x=input("enter year: ")
print("your age: " + str(int(2020) - int(x)))

#print(2020 - 1986)

#calculate and print days,months and weeks in 27 years
print("\n calculate and print days,months and weeks in 27 years")
days = 365 * 27
print("Days: " + str(int(days)))

weeks = 52 * 27
print("Weeks: " + str(int(weeks)))

months = 12 * 27
print("Months: " +str(int(months)))

#calculate area of circle with a radius of 5 units
print("\n calculate area of circle with a radius of 5 units")
import math
#print(math.pi)
area = math.pi * (5**2)
print("Area of Circle: "+str(float(area)))