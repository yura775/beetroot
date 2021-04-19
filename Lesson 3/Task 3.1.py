phrase = str(input('Make a sentence'))
length = len(phrase)
xlength = length - 2
if length < 2:
    print('Empty string')
else:
    print(phrase[0:2] + phrase[xlength:length])
