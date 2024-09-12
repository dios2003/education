# Задание "Они все так похожи"
import math


class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        self.__sides = __sides
        self.__color = list(__color)
        self.filled = bool
        super().__init__()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.filled = False
        if r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
            self.filled = True
            return self.filled

    def set_color(self, r, g, b):
        Figure.__is_valid_color(self, r, g, b)
        if self.filled:
            self.__color = []
            self.__color.append(r)
            self.__color.append(g)
            self.__color.append(b)
        return self.__color

    def __is_valid_side(self, list_new_sides):
        positive_integer = 0
        for i in range(0, len(list_new_sides)):
            if isinstance(list_new_sides[i], int) and list_new_sides[i] > 0:
                positive_integer += 1
        if len(list_new_sides) == self.__class__.sides_count and positive_integer == len(list_new_sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        count = 0
        if isinstance(self.__sides, tuple):
            list_sides = self.__sides
            while isinstance(list_sides, tuple):
                list_new_sides = []
                for i in range(0, len(list_sides)):
                    list_new_sides = list_sides[i]
                list_sides = list_new_sides
            self.__sides = list_sides
        if isinstance(self.__sides, int):
            for i in range(0, self.__class__.sides_count):
                count += self.__sides
            self.__sides = count
        if isinstance(self.__sides, list) and len(self.__sides) == 1:
            for i in range(0, self.__class__.sides_count):
                count += self.__sides[0]
            self.__sides = count
        if isinstance(self.__sides, list) and len(self.__sides) == self.__class__.sides_count:
            for i in range(0, self.__class__.sides_count):
                count += self.__sides[i]
            self.__sides = count
        return self.__sides

    def set_sides(self, *new_sides):
        list_new_sides = list(new_sides)
        list_sides = []
        if Figure.__is_valid_side(self, list_new_sides):
            for i in range(0, self.__class__.sides_count):
                list_sides.append(list_new_sides[i])
            self.__sides = list_sides
        if not Figure.__is_valid_side(self, list_new_sides):
            for i in range(0, self.__class__.sides_count):
                list_sides.append(1)
        return


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        self.__radius = __sides[0]
        self.__square = 0
        super().__init__(__color, __sides)

    def get_square(self):
        self.__square = self.__radius / 2 * math.pi
        return self.__square


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        self.__sides = __sides
        self.__volume = 0
        super().__init__(__color, __sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        list_sides = []
        list_new_sides = list(new_sides)
        if len(list_new_sides) > 1 and len(list_new_sides) != self.__class__.sides_count and len(self.__sides) == 1:
            for i in range(0, self.__class__.sides_count):
                list_sides.append(self.__sides[0])
        self.__sides = list_sides
        Figure.__sides = list_sides
        return

    def get_volume(self):
        self.__volume = self.__sides[0] ** 3
        return self.__volume


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        self.__sides = __sides
        self.__square = 0
        self.__p = int()
        super().__init__(__color, __sides)

    def get_square(self):
        list_sides = []
        if not isinstance(self.__sides, int) and len(self.__sides) == 1:
            for i in range(0, self.__class__.sides_count):
                list_sides.append(self.__sides[0])
            self.__sides = list_sides
        if not isinstance(self.__sides, int) and len(self.__sides) == self.__class__.sides_count:
            self.__p = Figure.__len__(self)/2
            self.__square = math.sqrt((self.__p*(self.__p - self.__sides[0]) * (self.__p - self.__sides[1]) *
                                       (self.__p - self.__sides[2])))
        return self.__square


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 12)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)   # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
