# 📚 Python Library Management System (OOP Mini Project)

A simple object-oriented library management system built in Python.  
The project demonstrates all fundamental OOP concepts:

- Classes & objects  
- Inheritance  
- Method overriding  
- Polymorphism  
- Composition  
- Special methods (`__str__`, `__len__`)  
- Filtering and searching  

This is an educational mini-project designed to help beginners practice OOP in a clean, structured way.

---

## 🚀 Features

### ✔ Add books to the library  
Supports multiple types of books:
- `Book` (base class)
- `FictionBook` (inherits from Book)
- `ScienceBook` (inherits from Book)

### ✔ Search functionality
- Search by title  
- Search by author  

### ✔ Filtering
- Get all fiction books  
- Get all science books  

### ✔ Remove books by title

### ✔ Advanced OOP structure
- Includes an abstract class `Shape` and implementations (`Circle`, `Rectangle`) to demonstrate abstraction separately.

---

## 🧩 Example Usage

```python
lib = Library()

# Create books
b1 = Book("Dune", "Frank Herbert", 1965)
b2 = FictionBook("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")
b3 = ScienceBook("A Brief History of Time", "Stephen Hawking", 1988, "Physics")

# Add books
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

# Print total books
print(len(lib))  # 3

# List all fiction books
for book in lib.get_fiction():
    print(book)

# Remove a book
lib.remove_book("Dune")
print(len(lib))  # 2
