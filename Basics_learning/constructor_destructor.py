class Dog:
    x = 0
    name = ""

    def __init__(self, n):
        name = n
        print("Name of dog is " + name)

    def dmethod(self):
        self.x = self.x + 1
        print("Count of Dog is:", self.x)

    def __del__(self):
        print("This is destructor")


d = Dog("Tojo")
d.dmethod()
d.dmethod()
c = Dog("Gogo")
c.dmethod()
