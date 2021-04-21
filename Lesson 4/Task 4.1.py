import random

num=random.randint(1, 10)
guess=int(input('Try to guess what number is in my mind, lets play from 1 to 10  '))
if guess > 10:
    print('You will never win with numbers bigger than 10...')
elif num != guess:
    print('sorry, you lose. Nothing personal')
else:
    print('congratulations! you win')