class Shape:
    def __init__(self):
        pass
    def area_of_figure(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area_of_figure(self):
        return self.length * self.length

a = Square(3)
print(a.area_of_figure())