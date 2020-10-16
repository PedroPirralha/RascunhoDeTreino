

word = input('digite uma palavra .:')

wordAdd = []

for x in word:
    wordAdd.append(x)

for n in wordAdd[::-1]:
    print(n,end='')
    
print('\n')