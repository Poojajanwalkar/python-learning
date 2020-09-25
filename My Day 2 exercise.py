hourly_wage = 20.00
hours_worked = 40

print(hourly_wage * hours_worked)

x = 8.00
y = 6.99
print(x + y)

print("what is your age?")
input()

#Ask the user for their name and age, assign theses values to two variables
print("\n  Ask the user for their name and age, assign theses values to two variables")
name = input("Please enter your name: ")
print("Name: " + name)

age = input("Enter your age?")
print("Age: " + age)

#Investigate what happens when you try to assign a value to a variable that you’ve already defined
print("\n Investigate what happens when you try to assign a value to a variable that you’ve already defined")
x = 10.0
print(x)
print("\n x=10.0")
x = 0.001
print("\n x = 0.001")
print(x)

#debugging
print("\n debugging")
hourly_wage = input("Please enter your hourly wage: ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ")