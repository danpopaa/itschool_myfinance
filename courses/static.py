class OurClass:
    x2 = 5
    y2 = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_sum(self):
        return self.x + self.y

    @staticmethod
    def get_prod():
        return OurClass.x2 * OurClass.y2

    @classmethod
    def get_prod2(cls):
        return cls.get_prod()


s = OurClass(5, 3)
print(s.get_sum())

s2 = OurClass(6, 3)

print(s.get_prod2())
OurClass.x2 = 6
print(s2.get_prod2())

