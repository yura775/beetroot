import random

f=random.sample(range(1,11),10)
s=random.sample(range(1,11),10)
w=(set(f)|set(s))
print('All duplicates were cleared:',w)