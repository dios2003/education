#Задача "Мифическое наследование"

class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound
        super().__init__()

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        x_y = (int(self.x_distance), int(self.y_distance))
        return x_y

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()