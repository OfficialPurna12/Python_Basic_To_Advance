 #Write a program that takes user input for year of birth (as a string) in the format 'YYYY’ 


from datetime import datetime

#current year 

current_year = datetime.now().year

#user input

birth_year = input("Enter your year of birth in the format 'YYYY' : ")

#calculate age

age = current_year - int(birth_year)

print(f"You are {age} years old.")


