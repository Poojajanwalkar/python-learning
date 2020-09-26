hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: " + hourly_wage)
print("Hours worked: " + hours_worked)

output = "{} is {} years old.{} works as {}".format("John", 24, "John", "Web deveop")
print(output)

output = "{0} is {1} years old.{0} works as {2}"
print(output.format("John", 24, "Web devop"))

output= "{name} is {age} years old.{name} works as{job}"
print(output.format(name="John", age=23,  job="designer"))

name= "Poll"
age=56
print("{}  is  {} years old.".format(name,age))

print(f"{name} is {age} years old." + " :Added f-string")

#prints the person's name and age in months
print("\n prints the person's name and age in months")
print(f"{name} is {age * 12} months old!")

# Exercises

print("\n string concatenation, format, or f-strings")
greeting = "Hello, world{}"
print(greeting.format("!"))
# adding f-string
x = "!"
print(f"Hello World{x}")

#Ask the user for their name, and then greet the user
name = input("Enter your name: ")
x = "!"
print(f"Good Morning, {name}{x}  ".strip())
print("Good Afternoon, {}{}".format(name,x))

#Concatenate the string
z_age = 29
print("I am " + str(z_age))

#Format and print the information below using string interpolation
title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(f"{title} ({release_year}), directed by {director}")