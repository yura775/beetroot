class Person:
    def __init__(self, first_name, last_name, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def talk (self):
        print(f'Hello! My name is {self.first_name} {self.last_name} and I am {self.age} years old')

Carl_Johnson = Person('Carl', 'Johnson', 27)
Carl_Johnson.talk()