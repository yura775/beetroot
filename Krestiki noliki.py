import random
print('You are playing for X')
gb = [['_', '_', '_'],
      ['_', '_', '_'],
      ['_', '_', '_']]
while True:
    row= int(input('Enter row number:'))
    column= int(input('Enter column number:'))
        if row >2 and column >2:
            print('Please choose numbers from 0 to 2')
            continue
        if gb[row] [column] == '_':
            gb[row] [column]='Х'
            break
        else:
            continue
    while True:
        crow = random.randint(0, 2)
        ccolumn = random.randint(0, 2)
        if gb[crow][ccolumn] == '_':
            gb[crow][ccolumn] = 'O'
        break

print(gb)








