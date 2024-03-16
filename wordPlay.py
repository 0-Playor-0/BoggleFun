import csv

#Working with the word list
word_list = open('4000-words.csv')
readFile = csv.reader(word_list)

words = []
for word in readFile:
    words.append(word[0])

#Words are stored in a list, as a list

def checkifEngWord(word):
    print(word)
    if word not in words:
        print("Not an english word or not in dataset")
        return False
    else:
        print("Nice word, continue!")
        return True

 