import random

f=random.sample(range(1,101),100)
e = 0
n = f[e]
i = []
while e<=100:
    if n %7==0 and not n %5==0:
        i.append(n)
    e=(e+1)
print(i)
