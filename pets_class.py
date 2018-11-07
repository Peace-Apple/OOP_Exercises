class Pets:
    kind = "mammals"

    def __init__(self, age, name):
        self.age = age
        self.name = name

class Dog:
    dogs = ["Tom", "Fletcher", "Larry"]

    num = len(dogs)

    print("I have {} dogs.".format(num))

    first = Pets(6, 'Tom')

    second = Pets(7, 'Fletcher')
    
    third = Pets(9, 'Larry')

    print("{} is {}.".format(first.name, first.age))
    print("{} is {}.".format(second.name, second.age))
    print("{} is {}.".format(third.name, third.age))
    print("And they're all {}, of course.".format(Pets.kind))
    