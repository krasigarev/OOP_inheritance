class Animals:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Dog(Animals):
    def __init__(self, name, age, number_of_legs):
        Animals.__init__(self, name, age)
        self.number_of_legs = number_of_legs

    def make_sound(self):
        return f"bau bau"

    def __str__(self):
        return f"Dog: {self.name}, age: {self.age}, number of legs: {self.number_of_legs}"

class Cat(Animals):
    def __init__(self, name, age, intelligence_quotient):
        Animals.__init__(self, name, age)
        self.intelligence_quotient = intelligence_quotient

    def make_sound(self):
        return f"myau myau"

    def __str__(self):
        return f"Cat {self.name}, Age: {self.age}, intelligence quotient: {self.intelligence_quotient}"

class Snake(Animals):
    def __init__(self, name, age, cruelty_coefficient):
        Animals.__init__(self, name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def make_sound(self):
        return f"ssss ssss"

    def __str__(self):
        return f"Snake {self.name}, age: {self.age}, Cruelty: {self.cruelty_coefficient}"

data_list = input().split()
animals_list = []

while not data_list[0] == "Im your Huckleberry":
    if data_list[0] == "talk":
        name = data_list[1]
        current_animal = list(filter(lambda a: a.name == name, animals_list))[0]
        print(current_animal.make_sound())
    else:
        kind = data_list[0]
        name = data_list[1]
        age = data_list[2]
        item = data_list[3]
        if kind == "Dog":
            dog = Dog(name, age, item)
            animals_list.append(dog)
        elif kind == "Cat":
            cat = Cat(name, age, item)
            animals_list.append(cat)
        elif kind == "Snake":
            snake = Snake(name, age, item)
            animals_list.append(snake)
    
    data_list = input().split()
