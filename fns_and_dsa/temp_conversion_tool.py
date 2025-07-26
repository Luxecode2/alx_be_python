# temp_conversion_tool.py

# ✅ Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using global conversion factor.
    """
    # Demonstrates variable scope (reading global variable)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using global conversion factor.
    """
    # Demonstrates variable scope (reading global variable)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ✅ Main program logic with user interaction
if __name__ == "__main__":
    try:
        # Prompt user to enter a numeric temperature
        user_input = input("Enter the temperature to convert: ").strip()
        temperature = float(user_input)

        # Prompt user to enter the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
