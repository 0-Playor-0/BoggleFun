#Imports
import wordPlay as doc
import basicui as ui
import points
import algo

#Handling Data
words = doc.words


ui.showUI()
while True:
    cont = str(input("Would you like to continue?"))
    if cont=="no" or cont == "No":
        break
    else:
        algo.algo()


print(algo.foundWords)
 

points.calculate_total(algo.foundWords)