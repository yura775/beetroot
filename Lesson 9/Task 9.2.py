import json

class Phonebook:
    pb = {}
    def __init__(self,  add, search, delete, update):
        self.add = add
        self.search = search
        self.delete = delete
        self.update = update
    def add (self):
        print('You are going to add new contact to your phonebook')
        name = input('Please enter the name: ')
        surname = input('Please enter the surname: ')
        telephone_number = input('Please enter the phone number: ')
        city = input('Please enter the city: ')
        pb.pop({'Name': name, 'Surname': surname, 'Number': telephone_number, 'City': city})
    def search (self):
        pass
    def delete (self):
        pass
    def update (self):
        pass
Phone = Phonebook

def main_menu(Phone):
    user_input = int(input('Hello and welcome to the phonebook! What are you going to do next?\n'
                             '   1. Add new contact\n'
                             '   2. Search contact\n'
                             '   3. Delete contact\n'
                             '   4. Update contact\n'
                             '   5. Exit program\n'
                            'So what is your choice? Pick a number '))
    while True:
        if user_input == 1:
             Phone.add()
        elif user_input == 2:
             Phone.search()
        elif user_input == 3:
             Phone.delete()
        elif user_input == 4:
             Phone.update()
        elif user_input == 5:
            print(' Thank you for using our Phonebook')
            break
        else:
            print ('Wrong number')

main_menu()
print(pb)
