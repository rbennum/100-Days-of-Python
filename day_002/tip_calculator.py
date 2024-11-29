print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = float(input("How many people to split the bill? "))
final_calc = total_bill * (1 + tip_percentage / 100) / total_people
print(f"Each person should pay: ${round(final_calc, 2)}")