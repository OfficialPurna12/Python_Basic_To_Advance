# Example Here: 
# write a code to store the library  books add a library_name, total book, book name, average rating, author name, location, publisher, contact number open, close time, time and price of the book.


totals_book = 5000
average_rating = 5.5
book_name = ["Python", "Java", "C++", "C", "C#", "Ruby", "PHP", "JavaScript", "HTML", "CSS"]
author_name = "Bishwaraj Paudel"
location = (40.46, -73.58, "Pokhara")
publisher = "Bishwaraj Paudel"
contact_details = {
    "email": "bishwaraj@paudel.com",
    "phone": "9846612345"

}
open_time = "8:00 AM"
close_time = "5:00 PM"

price = {
    "Python": "$110",
    "Java": "$100",
    "C++": "$90",
    "C": "$80",
    "C#": "$70",
    "Ruby": "$60",
    "PHP": "$50",
    "JavaScript": "$40",
    "HTML": "$30",
    "CSS": "$20"
}

# printing the details of the library information:

print("Welcome to the Poudel Library Store !")
print("\n")
print("Here are the details of the library:")
print("\n")

print(f"Total number of books: {totals_book}")
print(f"Average rating: {average_rating}")
print(f"Book name: {book_name}")
print(f"Author name: {author_name}")
print(f"Location: {location}")
print(f"Publisher: {publisher}")
print(f"Contact details: {contact_details}")
print(f"Open time: {open_time}")
print(f"Close time: {close_time}")
print(f"Price: {price}")
print("\n")

print("Thank you for visiting Poudel Library Store ! and  see you soon !")

# Output:
# Welcome to the Poudel Library Store !
# Here are the details of the library:

# Total number of books: 5000
# Average rating: 5.5
# Book name: ['Python', 'Java', 'C++', 'C', 'C#', 'Ruby', 'PHP', 'JavaScript', 'HTML', 'CSS']
# Author name: Bishwaraj Paudel
# Location: (40.46, -73.58, 'Pokhara')
# Publisher: Bishwaraj Paudel
# Contact details: {'email': 'bishwaraj@paudel.com', 'phone': '9846612345'}
# Open time: 8:00 AM
# Close time: 5:00 PM
# Price: {'Python': '$110', 'Java': '$100', 'C++': '$90', 'C': '$80', 'C#': '$70', 'Ruby': '$60', 'PHP': '$50', 'JavaScript': '$40', 'HTML': '$30', 'CSS': '$20'}
