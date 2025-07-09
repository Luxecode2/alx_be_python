# finance_calculator.py

# Prompt the user for monthly income and expenses
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate annual savings with 5% interest
annual_savings = monthly_savings * 12 * 1.05

# Display the results with 2 decimal formatting
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
