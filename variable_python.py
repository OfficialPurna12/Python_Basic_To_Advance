# Personal Information
name = "Purna Bahadur Khatri"
age = 22
phone = "9829845767"

print(f"My name is {name} and I am {age} years old. My phone number is {phone}.")

# User Interface
name = input("Enter your name: ")
age = input("Enter your age: ")
phone = input("Enter your phone: ")

print(f"Your name is {name}, your age is {age}, and your phone number is {phone}.")

# Find Difference Between Income and Expense
income = int(input("Enter your income: "))
expense = int(input("Enter your expense: "))
diff = income - expense

print(f"Your income is {income}, your expense is {expense}, and the difference is {diff}.")

# Basic Calculation of Python
first_number = 10
second_number = 20

sum_result = first_number + second_number
sub_result = first_number - second_number
mul_result = first_number * second_number
div_result = first_number / second_number

# Modulo is used to get the remainder of the division
mod_result = first_number % second_number
individ_result = first_number // second_number
square_result = first_number ** second_number

# Display the results
print(f"Sum of numbers: {sum_result}")
print(f"Subtraction of numbers: {sub_result}")
print(f"Multiplication of numbers: {mul_result}")
print(f"Division of numbers: {div_result}")
print(f"Modulo (remainder): {mod_result}")
print(f"Integer division: {individ_result}")
print(f"Square of the number: {square_result}")


# Challenge 1:
#Write down what you spend each day from Sunday to Saturday, add them up to find the total forthe week, and figure out the average amount spent per day.


#collecting expenses data ?

sunday = int(input("Enter your expenses on Sunday: "))
monday = int(input("Enter your expenses on Monday: "))
tuesday = int(input("Enter your expenses on Tuesday: "))    
wednesday = int(input("Enter your expenses on Wednesday: "))
thursday = int(input("Enter your expenses on Thursday: "))
friday = int(input("Enter your expenses on Friday: "))
saturday = int(input("Enter your expenses on Saturday: "))

total_expenses = sunday + monday + tuesday + wednesday + thursday + friday + saturday
average_expenses = total_expenses / 7

print("Weekly speedily summary") 
print(f"Total Spending for the week: {total_expenses}")
print(f"Average Spending per day: {average_expenses}")


# challenge 3:
# write a program that calculates the area of a rectangle and a triangle. The program should ask the user to enter the width and height of the rectangle and the base and height of the triangle. The program should then display the area of the rectangle and the triangle.

# Area of a rectangle = width * height
# Area of a triangle = 1/2 * base * height

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area_rectangle = width * height
area_triangle = 1/2 * base * height

print(f"The area of the rectangle is: {area_rectangle}")
print(f"The area of the triangle is: {area_triangle}")

# challenge 4: 
# Write a program that calculates the area of a circle. The program should ask the user to enter the radius of the circle, and then display the area of the circle.

radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14159 * radius ** 2
print(f"The area of the circle is: {area_circle}")