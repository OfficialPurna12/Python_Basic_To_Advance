# Write a program that checks if a given number is even or odd. Take user input for the number,perform the check, and print the result. Include comments explaining each part of the code.

# use of variable in odd even number 


number = 10 # variable number is assigned value 10

if number % 2 == 0: # if the number is divisible by 2 and the remainder is 0
    print("The number is even") # print the number is even
else:
    print("The number is odd") # print the number is odd

# This code input user interface to enter the number and check if the number is even or odd.

numbers = int(input("Enter a number : ")) # input the number from the user

if numbers %2 == 0: # if the number is divisible by 2 and the remainder is 0
    print("The number is even") # print the number is even
else:
    print("The number is odd") # print the number is odd


# write a code voter eligibility check

age = 18 # variable age is assigned value 18

if age >=18:
    print("You are eligible to vote") # print you are eligible to vote
else:    
    print("You are not eligible to vote") # print you are not eligible to vote


# This code input user interface to enter the age and check if the age is eligible to vote or not.

ages = int(input("Enter your age : ")) # input the age from the user

if ages >=18: # if the age is greater than or equal to 18
    print("You are eligible to vote") # print you are eligible to vote
else:
    print("You are not eligible to vote") # print you are not eligible to vote