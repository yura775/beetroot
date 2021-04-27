i_list = []
j_list = []
for a in range(1,11):
    i_list.append(a)
    j_list.append(a**2)
i = tuple(i_list)
j = tuple(j_list)
result = [i, j]
print(result)
