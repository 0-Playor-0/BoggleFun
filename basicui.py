import random
import time
import sys

#Let alphabet list have all alphabets A through Z
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Grid will be n*n
n = int(input("How big would you like the grid to be? "))

if n>100:
    print("You cannot have a grid that big, it must be lesser than 100.")
    sys.exit()
elif n<3:
    print("You cannot have a grid that small, it must be greater than 2.")
    sys.exit()
Grid = []

for i in range(n):
    row = []
    for x in range(n):
        row.append(random.choice(alphabets))
    Grid.append(row)

def showUI():
    for row in Grid:
        txt = "|"
        for letr in row:
            txt += (" " + letr +" |" )
        print(" "+"___ "*n)
        print (txt)
        print(" "+"--- "*n)
        


print(Grid)
    




