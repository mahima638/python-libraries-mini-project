# Importing the required library
import matplotlib.pyplot as plt

# Function to convert Celsius to Fahrenheit
def celcius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

# Function to convert Fahrenheit to Celsius (not used here, but good for reference)
def fahrenheit_to_celcius(f):
    return (f - 32) * 5 / 9

# List of Celsius values
celcius_values = [2, 4, 5, 1, 8, 7, 8, 4, 7]

# Convert each Celsius value to Fahrenheit using list comprehension
fahrenheit_values = [celcius_to_fahrenheit(c) for c in celcius_values]

# Plotting the Celsius vs Fahrenheit values
plt.plot(celcius_values, fahrenheit_values, marker='o', linestyle='-', color='b')

# Adding title and labels to the plot
plt.title('Celsius to Fahrenheit Conversion')
plt.xlabel('Celsius')
plt.ylabel('Fahrenheit')

# Display the plot
plt.show()
