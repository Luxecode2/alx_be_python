# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # so we can reuse it later

def calculate_future_date(current_date, days_to_add):
    """
    Calculates a future date by adding days_to_add to current_date.

    Args:
        current_date (datetime): The starting date.
        days_to_add (int): Number of days to add.

    Returns:
        datetime: The future date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

# --- Main script logic ---
if __name__ == "__main__":
    # Part 1: Display current date and time
    current = display_current_datetime()

    # Part 2: Ask user for number of days and calculate future date
    try:
        user_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current, user_input)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
