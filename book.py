class Book:
    def __init__(self,title,author):
        self.title =title
        self.author =author
    def __str__(self):
        return f"Book:{self.title} by {self.author}"
    def display(self):
        print(self.title)
        print(self.author)
    def __repr__(self):
        return f"Book (title={self.title},author={self.author})"
b1=Book("book","Suraj")
print(b1)
print(repr(b1))
        