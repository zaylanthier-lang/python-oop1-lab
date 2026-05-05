#!/usr/bin/env python3

class Coffee:
    # Create a new Coffee object with a size and price
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # Make sure size is Small, Medium, or Large
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large.")

    # Add a tip to the coffee price
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1