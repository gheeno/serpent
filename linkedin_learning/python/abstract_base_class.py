from abc import abstractmethod, ABC

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * ( self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, sides):
        self.sides = sides
    
    def calc_area(self):
        return self.sides * self.sides
    

c = Circle(2)
s = Square(3)

print(c.calc_area())
print(s.calc_area())