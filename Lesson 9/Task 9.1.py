with open('myfile.txt', 'w') as f:
    f.write('Hello my file world!')
file = open('myfile.txt', 'r')
print(file.read())
file.close()