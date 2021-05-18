class Fruit:
    def __init__(self, name):
        self.name = name
        print("Name of the fruit is ", name)

    def nutrition(self, n):
        print("Nutrition value of the fruit contain vitamin:", n)

    def fruit_shape(self, s):
        print("Shape of the fruit is:", s)


class Mango(Fruit):
    def nutrition(self):
        super(Mango, self).nutrition("A")
        print("Mango also contain Vitamin D")

    def color(self, c):
        print("Color of Mango is:", c)


f = Fruit("Orange")
f.nutrition("E")
f.fruit_shape("round")

m = Mango("Mango")
m.nutrition()
m.color("yellow")
