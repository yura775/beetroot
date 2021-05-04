import random

word=str(input('Tell me any word '))
num=len(word)
i=0 #helps to calculate
while i<5:
    def split(word):
        return list (word)
    letters=(split(word))
    var=(random.sample(letters, num)) #create list out of the letters
    ber=''.join(var) #create a string out of the list
    print(ber)
    i=(i+1)


