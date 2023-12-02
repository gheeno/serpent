class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price 

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def get_book_page_count(self):
        results = 0 
        for ch in self.chapters:
            results += ch.pagecount
        return results

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.99, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.get_book_page_count())
