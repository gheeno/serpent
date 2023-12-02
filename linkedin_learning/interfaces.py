from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape, Printable):
    # def draw(self):
    #     print("Drawing a circle")

    # def print_info(self):
    #     print("Printing...")
    def draw(self):
        return "from shape, drawing a circle"
    
    def print_info(self):
        return "Printing..."


c = Circle()
print(c.draw())
print(c.print_info())