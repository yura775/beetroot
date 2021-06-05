a = input('Please type the first number ')
b = input('Please type the second number ')

def my_func(q, w):
    try:
        s = int(q)**2/int(w)
    except TypeError and ValueError:
        print('you should use only numbers')
    except ZeroDivisionError:
        print('Do not divide by zero again')
    else:
        print(s)


my_func(a, b)