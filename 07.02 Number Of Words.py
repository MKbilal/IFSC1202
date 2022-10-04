def words (string):    
    x = 0
    for i in range(0, len(string)):
        if string[i] == ' ':
            x += 1
    return x
string = input('Enter a string: ')
print(words(string)+1, 'Words')