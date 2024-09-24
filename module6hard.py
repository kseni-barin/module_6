#Задание "Они все так похожи"

class Figure:
    sides_count = 0
    def __init__(self, color, *args, filled = False):
        self.__color = list(color) # список цветов в формате RGB
        self.__sides = list(*args) # список сторон (целые числа)
        self.filled = filled # закрашенный, bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        counts = 0
        for element in (r, g, b):
            if isinstance(element, int) and 0 <= element <= 255:
                counts +=1
        if counts == 3:
            return True
        else:
            return False

    def set_color(self, r, g, b):
       if self.__is_valid_color(r, g, b):
           self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if all(element > 0 and isinstance(element, int) for element in args) and len(args) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        if self.__is_valid_sides(*self.__sides):
            return self.__sides
        else:
            self.__sides = [1]*self.sides_count
            return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            for i in range(0, self.sides_count):
                self.__sides[i] = new_sides[i]

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *args):
        super().__init__(color, args)
        side = self.get_sides()
        if len(side) == Circle.sides_count and all(isinstance(element, int) for element in side):
           side_1 = side
        else:
            side_1 = [1]
        self.__radius = side_1[0] / 6.28

    def get_square(self):
        return 3.14*self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *args):
        super().__init__(color, args)

    def get_square(self):
        sides_3 = self.get_sides()
        p = sum(sides_3)/2
        return (p*(p - sides_3[0])*(p - sides_3[1])*(p - sides_3[2]))**0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *args):
        super().__init__(color = color)
        if len(list(args)) == 1:
            c = list(args)
        else:
            c = [1]
        self.__sides = c*12

    def __is_valid_sides(self, *args):
        if all(element > 0 and isinstance(element, int) for element in args) and len(args) == 1:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)*12

    def get_volume(self):
        return self.__sides[0]**3

