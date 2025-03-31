class Person:
    name = "Anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Hiral")
print(p1.name)