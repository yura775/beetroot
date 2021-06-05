class countries:
    mame=None
    population=None
    GDP=None
    language=None

    def __init__(self, name, population, GDP, language):
        self.name = name
        self.population = population
        self.GDP = GDP
        self.language = language

    def contry_name (self):
        print(f'Информация о {self.name}, где {self.population} людей говорят на {self.language}' )

countrie_object = countries('Ukraine', 37000000, 23423465, 'ukrainian')
countrie2_object= countries('USA', 123234234, 23423425345, 'English')
countrie2_object.contry_name()