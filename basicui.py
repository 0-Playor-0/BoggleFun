import random
import time

#Let alphabet list have all alphabets A through Z
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Grid will be n*n
n = int(input("How big would you like the grid to be? "))

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
    




