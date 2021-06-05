

def make_operations (operator, *args):
    p=args[0]
    for i in range(1,len(args)):
        p=eval(f'{p}{operator}{args[i]}')
    print(p)
    print(operator, *args)

make_operations('+',7,7,2)
make_operations('-',5,5,-10,-20)
make_operations('*',7,6)

