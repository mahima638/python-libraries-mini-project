import matplotlib.pyplot as plt
def celcius_to_fahrenheit(c):
  return (c*9/5)+32
def fahrenheit_to_celcius(f):
  return (f-32) * 5/9
  
celcius_values =[2, 4,5,1,8,7,8,4,7]
fahrenheit_values =[celcius_to_fahrenheit(c) for c in celcius_values]
plt.plot(celcius_values, fahrenheit_values, marker='o', linestyle='-', color='b')
plt.title('Celcius to Fahrenheit Conversion')
plt.xlabel('Celcius')
plt.ylabel('Fahrenheit')
plt.show()
print("Hello")
