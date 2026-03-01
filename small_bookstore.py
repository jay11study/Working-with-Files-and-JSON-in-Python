#Task 1 — Read the Inventory

#code
import json

with open("inventory.json", "r") as f:
    inventory = json.load(f)

print("Total books: ", len(inventory))

#Explanation
#The file - inventory.json is opened in read mode using a "with" block.
#json.load(f) converts the JSON data from the file into a Python dictionaries.
#len(inventory) calculates the total number of books in the list.



#Task 2 — Update and Save

#Code
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

inventory.append(new_book)

with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=4)


#Explanation
#A new dictionary - new_book is created for the new book.
#The append() is used to add the new book to the existing inventory list.
#The file is opened in write mode which overwrites the existing file along with the new book.
#json.dump() converts the updated Python list back into JSON format and writes it to the file.
#indent=4 ensures the JSON file is formatted neatly and is readable.


#Task 3 — Display the Updated Inventory

#Code
with open("inventory.json", "r") as f:
    updated_inventory = json.load(f)

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")
  
#Explanation
#The updated file is reopened in read mode.
#json.load() converts the JSON data into a Python list.
#A for loop iterates through each book in the list.
#f-strings are used to format and print each book’s details in the required format.
