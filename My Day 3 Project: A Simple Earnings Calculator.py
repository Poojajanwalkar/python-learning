emp_name = input("Enter your name: ").strip().title()
hourly_wage = int(input("Enter your Hourly wage : "))
total_hours= int(input("How many hours you worked this week : "))
total_amount= str(hourly_wage * total_hours)
print(f"{emp_name} earned {total_amount} this week.")
