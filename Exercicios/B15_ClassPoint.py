





class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.get_x():2d},{self.get_y():2d})"

    def get_x(self):
        return self.x

    def set_x(self, n_x):
        if type(n_x) == int:
            self.x = n_x
        else:
            print("Valor não é um numero")

    def get_y(self):
        return self.y

    def set_y(self, n_y):
        if type(n_y) == int:
            self.y = n_y
        else:
            print("Valor não é um numero")

if __name__ == '__main__':
    print('')
    print("~(1)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('')

    p1 = Point()
    p2 = Point(2,3)
    p3 = Point(4)
    p4 = Point(y=6)

    print('P1:',p1)
    print('')
    print('P2:',p2)
    print('')
    print('P3:',p3)
    print('')
    print('P4:',p4)

    print('')
    print("~(2)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    p3.set_y(5)

    print('P3:',p3)





