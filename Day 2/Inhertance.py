class Vehicle(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Lambo(Vehicle):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def info(self):
        return "this is my " + self.color + " color " + self.name + " of " + str(self.age) + " years old"


mycar = Lambo("Lambo", 3, "red")
print(mycar.info())
