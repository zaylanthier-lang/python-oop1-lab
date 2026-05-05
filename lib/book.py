#!/usr/bin/env python3

class Book:
    # Initialize a Book with a title and page count
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter to validate that page_count is an integer
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer.")

    # Simulates turning a page in the book
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")