
print("Welcome to Tip Calculator ")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12 or 15? "))
people=int(input("How many people to split the bill? "))
total=bill*(1+(tip/100))
total_pay=round((total/people),2)
print("Each person should pay: $",total_pay)
