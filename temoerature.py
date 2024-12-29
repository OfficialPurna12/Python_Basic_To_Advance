#Write a program that takes user input for a temperature in Celsius and converts it to Fahrenheit. Perform the conversion and print the result. Include comments explaining each part of the code.

celsius = float(input("Enter the temperature in Celsius: ")) # This line takes user input for the temperature in Celsius and converts it to a float

fahrenheit = (celsius * 9/5) + 32 # This line converts the temperature from Celsius to Fahrenheit

print(f"The temperature in Fahrenheit is: {fahrenheit}") # This line prints the temperature in Fahrenheit


# References:
# https://en.wikipedia.org/wiki/Fahrenheit

# Write a program that takes user input for a number and checks if it is positive, negative, or zero. Perform the check and print the result. Include comments explaining each part of the code

number = float(input("Enter a number: ")) # This line takes user input for a number and converts it to a float

if number > 0: # This line checks if the number is greater than zero
    print("The number is positive") # This line prints the result if the number is positive
elif number < 0: # This line checks if the number is less than zero
    print("The number is negative") # This line prints the result if the number is negative
else: # This line is executed if the number is zero
    print("The number is zero") # This line prints the result if the number is zero