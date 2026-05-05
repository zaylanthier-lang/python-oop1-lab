from book import Book
from coffee import Coffee

book = Book("Python Basics", 120)
coffee = Coffee("Medium", 4)

book.turn_page()

print(coffee.price)
coffee.tip()
print(coffee.price)