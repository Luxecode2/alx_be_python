# daily_reminder.py

# Loop to ensure the user enters valid input
while True:
    # Prompt for task description
    task = input("Enter your task: ").strip()

    # Prompt for priority and validate
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter high, medium, or low.\n")
        continue

    # Prompt for time-bound status and validate
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time-bound. Please enter yes or no.\n")
        continue

    # If all inputs are valid, break out of loop
    break

# Use match-case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"

# Use if to check if it's time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Output the final customized reminder
print("\n" + reminder)
