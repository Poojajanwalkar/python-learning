age = int(input("How old are you? "))

if age < 18:
	  print("Sorry, we can't serve you.")
	  
name = input("Check you name with our system available: ")

if name == "pooja":
	print(f"Welcome ({name})")

#Exercises:
	#1) Try to approximate the behaviour of the is operator using = 
sub_A = ["A", "B", 1, 2.0]
sub_B = ["A", "B", 1, 2.0]

print(sub_A == sub_B)
print(id(sub_A) == id(sub_B))

sub_B = sub_A
print(id(sub_A) == id(sub_B))

sub_B = sub_A
print(sub_A is sub_B)
#2)Try to use the is operator or the id function to investigate the difference between this:
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(new_numbers)
print("numbers ID : " + str(id(numbers)))
print("new_numbers ID: " + str(id(new_numbers)))
print( numbers is new_numbers)

#After appending :
numbers = [1, 2, 3, 4]
numbers.append(5)
print("\n After appending with 5 number : " + str(numbers))

print("\n appended with 5 numbers ID: " + str(id(numbers)))
print(" new_numbers ID: " + str(id(new_numbers)))

print("\n below appended number 5  investigate with is operator:")
print(numbers is new_numbers)

#3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
number = int(input("Enter a number: "))
print("Entered number: " + str(number)) 	  
if number > 0:
	print(f"Your number {number} is Positive")
elif number < 0:
	 print(f"Your number {number} is Negative")
elif number == 0:
	 print(f"Your number {number}")

#4)Write a program to determine whether an employee is owed any overtime
#ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
employee_hours = int(input("How many hours you worked this week: "))
hourly_wages = float(input("Enter your Hourly wages: "))
basic_salary = employee_hours * hourly_wages
overtime_salary =(employee_hours - 40) * hourly_wages * 0.1 
if employee_hours <= 40:
	 print(f"your salary ${basic_salary}")

#If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due.
elif employee_hours > 40:
	 print(f"your salary ${basic_salary + overtime_salary} with overtime amount ")
