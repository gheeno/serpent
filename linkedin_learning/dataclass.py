from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

b1 = Book("Orange Book", "Mark Mansen", 123, 12.99)
b2 = Book("Make your bed", "William H. McRaven", 100, 10.99)

print(b1)
print(b2)
print(b1.title)
print(b1 == b2)