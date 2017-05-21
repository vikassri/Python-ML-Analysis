from clock import Clock
from calander import Calander


class Time(Calander, Clock):
    def __init__(self, day, month, year, hours=0, minutes=0, seconds=0):
        Calander.__init__(self, day, month, year)
        Clock.__init__(self, hours, minutes, seconds)

    def __str__(self):
        return Calander.__str__(self) + ", " + Clock.__str__(self)


if __name__ == '__main__':
    x = Time(24, 12, 57)
    print(x)
    for i in range(1000):
        x.tick()
    for i in range(1000):
        x.advance()
    print(x)
