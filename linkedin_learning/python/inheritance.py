class Publication:
  
  '''Super class'''

  def __init__(self, title, price):
    self.title = title
    self.price = price


class Book(Publication):
  
  '''Class to inherit super class'''

  def __init__(self, title, price, pages, author):
    super().__init__(title, price)
    self.author = author
    self.pages = pages


b1 = Book(title="Python Programming", price=500, pages=500, author="Zed Shaw")
print(b1.title)
print(b1.price)
print(b1.pages)
print(b1.author)
