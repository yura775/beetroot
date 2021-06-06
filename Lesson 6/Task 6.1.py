sentence = str(input('Give me any sentence'))
words = sentence.split() #Devide a sentence into words
unique_words = set(words) #clean from duplicates, create a set of keys
numbers = len(unique_words) #find out values
num_list = [] #list of values
for i in range(1, numbers+1):
    num_list.append(i)
result = zip(unique_words, num_list) #combine keys with values
result2 = dict(result) #create a dictionary
print('Your dictionary looks like that:', result2)