#!/usr/bin/env python3

class Coffee:
    # Initialize a Coffee with size and price
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter to ensure size is valid
    @size.setter
    def size(self, size):
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    # Adds a tip to the coffee price
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1