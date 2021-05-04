

def make_operations (operator, *kvargs):
    p=kvargs[0]
    for i in range(1,len(kvargs)):
        p=eval(f'{p}{operator}{kvargs[i]}')
    print(p)
    print(operator, *kvargs)

make_operations('+',7,7,2)
make_operations('-',5,5,-10,-20)
make_operations('*',7,6)
