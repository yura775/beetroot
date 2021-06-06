import random

first_num=random.randint(1, 100)
second_num=random.randint(1, 100)
print('Check this out', first_num, '+', second_num)
guess=int(input('Please write down the answer '))
if guess==first_num+second_num:
    print('Cool! You are so smart')
else:
    print('Not cool...')