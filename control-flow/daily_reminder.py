# daily_reminder.py

# Step 1: Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Customized reminder using match-case and if
match priority:
    case "high":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            message = f"Reminder: '{task}' is a high priority task. Try to address it as soon as possible."
    case "medium":
        if time_bound == "yes":
            message = f"Note: '{task}' is a medium priority task that should be done today if possible."
        else:
            message = f"Note: '{task}' is a medium priority task. Plan to do it sometime soon."
    case "low":
        if time_bound == "yes":
            message = f"Notice: '{task}' is a low priority task but still needs to be completed today."
        else:
            message = f"Note: '{task}' is a low priority task. Consider doing it when you have free time."
    case _:
        message = f"Warning: Unknown priority for task '{task}'. Please enter high, medium, or low."

# Step 3: Print the customized message
print("\n" + message)
