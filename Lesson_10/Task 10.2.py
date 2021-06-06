class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.age_factor = 7
    def human_age(self):
        print(f'Your sweet {self.age} years old {self.breed} named {self.name} is actually {self.age * self.age_factor} years old in human age')
dog_1 = Dog('Zlata', 'labrador', 2)
dog_2 = Dog('Kuba', 'labrador', 0.5)
dog_1.human_age()
dog_2.human_age()
