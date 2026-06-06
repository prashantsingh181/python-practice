class Shape:
    def area(self):
        raise NotImplementedError("method not implemented")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 * (self.radius**2)) / 7


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


def print_areas(shapes):
    if not isinstance(shapes, list):
        raise TypeError("shapes should be a list")

    for shape in shapes:
        if not isinstance(shape, Shape):
            raise TypeError("list should contain only Shape Object")
        print(f"{type(shape).__name__} area: {shape.area():.2f}")


shapes = [Circle(5), Rectangle(4, 6)]
print_areas(shapes)
