#initialize the variables
# 1. Arithmetic operators
num1 = 20
num2 = 10

# performing operations

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div  = num1 / num2
mod = num1 % num2
floor_div = num1 // num2
exp = num1 ** num2

# printing the results
print("Addition of two numbers is:", add)
print("Subtraction of two numbers is:", sub)    
print("Multiplication of two numbers is:", mul)
print("Division of two numbers is:", div)
print("Modulus of two numbers is:", mod)
print("Floor division of two numbers is:", floor_div)
print("Exponent of two numbers is:", exp)

# 2. Comparison operators

num1 = 20
num2 = 10

# performing operations

equal = num1 == num2
not_equal = num1 != num2
greater = num1 > num2
less = num1 < num2
greater_equal = num1 >= num2
less_equal = num1 <= num2

# printing the results
print("Is num1 equal to num2:", equal)
print("Is num1 not equal to num2:", not_equal)
print("Is num1 greater than num2:", greater)
print("Is num1 less than num2:", less)
print("Is num1 greater than or equal to num2:", greater_equal)
print("Is num1 less than or equal to num2:", less_equal)


# 3. Logical operators

num1 = 20
num2 = 10

# performing operations

and_op = num1 and num2
or_op = num1 or num2
not_op = not num1

# printing the results
print("AND operation of two numbers is:", and_op)
print("OR operation of two numbers is:", or_op)
print("NOT operation of num1 is:", not_op)

# 4. Assignment operators

num1 = 20
num2 = 10

# performing operations

initial_value = num1
num1 += num2
print("Value of num1 after addition is:", num1)

initial_value = num1
num1 -= num2
print("Value of num1 after subtraction is:", num1)

initial_value = num1
num1 *= num2
print("Value of num1 after multiplication is:", num1)

initial_value = num1
num1 /= num2
print("Value of num1 after division is:", num1)

initial_value = num1
num1 %= num2
print("Value of num1 after modulus is:", num1)

initial_value = num1
num1 //= num2
print("Value of num1 after floor division is:", num1)


## Write a program that takes the ages of two people as input from the user. Compare the irages using comparison operators (==, !=, >, <, >=, <=) and print messages indicating the results (e.g., "Person 1 is older than Person 2").


# taking input from the user
person1_age = int(input("Enter the age of person 1: "))
person2_age = int(input("Enter the age of person 2: ")) 

# comparing the ages
if person1_age == person2_age:
    print("Person 1 and Person 2 are of the same age.")
elif person1_age != person2_age:
    print("Person 1 and Person 2 are of different ages.")
elif person1_age > person2_age:
    print("Person 1 is older than Person 2.")
elif person1_age < person2_age:
    print("Person 1 is younger than Person 2.")
elif person1_age >= person2_age:
    print("Person 1 is older than or equal to Person 2.")
elif person1_age <= person2_age:
    print("Person 1 is younger than or equal to Person 2.")
else:
    print("Invalid input.")

# #Write a program that takes the age and citizenship status of a person as input from the
# user. Use logical operators (and, or, not) to determine if the person is eligible to vote
# (age >= 18 and is a citizen). Print an appropriate message based on the result.

# taking input from the user
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

# checking if the person is eligible to vote
if age >= 18 and citizen == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Write a program that initializes a list of books available in a library. Take the name of a
# book as input from the user and check if it is available in the library using membership
# operators (in, not in). Print a message indicating whether the book is available or not.

# list of books available in the library
books = ["Python Programming", "Java Programming", "C Programming", "JavaScript Programming"]

# taking input from the user
book_name = input("Enter the name of the book: ")

# checking if the book is available in the library
if book_name in books:
    print("The book is available in the library.")
else:
    print("The book is not available in the library.")
    

