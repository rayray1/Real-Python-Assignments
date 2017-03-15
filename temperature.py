# Assignment: Convert temperatures


# Celsius to Fahrenheit
def celsius_to_fahrenheit(num):
    fahrenheit_temp = num * (9/5) + 32
    return fahrenheit_temp


# Fahrenheit to Celsius
def fahrenheit_to_celsius(num):
    celsius_temp = (num - 32) * (5/9)
    return celsius_temp
