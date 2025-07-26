# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global conversion factor.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global conversion factor.
    
    Args:
        celsius (float): Temperature in Celsius.
    
    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program logic
if __name__ == "__main__":
    try:
        # Prompt user to enter temperature value
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Will raise ValueError if not a number

        # Prompt user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print("Invalid temperature. Please enter a numeric value.")
