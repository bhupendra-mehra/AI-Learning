# Mini Project

# Create a Book class with:

# title
# author
# pages

# Implement:

# __str__ → Display book information.
# __repr__ → Developer-friendly representation.
# __len__ → Return the number of pages.
# __eq__ → Compare books by title and author.

# Then:

# book1 = Book("Python", "John", 350)
# book2 = Book("Python", "John", 400)
# book3 = Book("AI", "Alice", 250)

# Test:

# print(book1)
# print(repr(book1))
# print(len(book1))
# print(book1 == book2)
# print(book1 == book3)

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title : {self.title} , Author : {self.author}, Pages : {self.pages}"

    def __repr__(self):
        return f"Book({self.title},{self.author},{self.pages})" 
        # instead use this ---> return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __len__(self):
        return self.pages
    
    def __eq__(self,other):
        return self.title+self.author+str(self.pages) == other.title+other.author+str(other.pages)
        # instead of above it should be 
        # return (
        #     self.title,
        #     self.author,
        #     self.pages
        # ) == (
        #     other.title,
        #     other.author,
        #     other.pages
        # )

    
book1 = Book("Python", "John", 350)
book2 = Book("Python", "John", 400)
book3 = Book("AI", "Alice", 250)


print(book1)
print(repr(book1))
print(len(book1))
print(book1 == book2)
print(book1 == book3)


# class Book:

#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"{self.title} by {self.author} ({self.pages} pages)"

#     def __repr__(self):
#         return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

#     def __len__(self):
#         return self.pages

#     def __eq__(self, other):
#         if not isinstance(other, Book):
#             return NotImplemented

#         return (
#             self.title,
#             self.author,
#             self.pages
#         ) == (
#             other.title,
#             other.author,
#             other.pages
#         )