task = input("Enter your task: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes or no): ").lower()


match priority:
    case "high":
        reminder = f"🔴 High Priority Task: '{task}'."
    case "medium":
        reminder = f"🟠 Medium Priority Task: '{task}'."
    case "low":
        reminder = f"🟢 Low Priority Task: '{task}'."
    case _:
        reminder = f"⚪ Task: '{task}' with unknown priority."

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print("\nYour Reminder:")
print(reminder)