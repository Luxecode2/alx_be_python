# finance_calculator.py

# Prompt the user for monthly income and expenses
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate annual savings with 5% interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(annual_savings) + ".")
