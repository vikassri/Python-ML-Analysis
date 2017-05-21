class A():
    def __init__(self):
        self.public = "Hey this is public"
        self._protected = "Hey this is protected"
        self.__private = "hey This is private"


class B:
    def p(self):
        a = A()
        print(a.public + ", my value can be changed")  # can be accessible from outside class and modified as well
        print(a._protected)                            # can be accessible
        print(a.__private)                             # can noot be accessible


if __name__ == '__main__':
    b = B()
    b.p()