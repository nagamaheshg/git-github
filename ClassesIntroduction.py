class Animal():
    def __init__(self):

        print('Animal Object is created')

    def who_am_i(self):

        print('I am animal')

    def eat(self):

        print('I am eating food')


class Dog(Animal):
    def __init__(self):

        Animal.__init__(self)

    def who_am_i(self):

        print('I am a dog')


animal = Animal()
animal.eat()
dog = Dog()
dog.eat()
dog.who_am_i()
