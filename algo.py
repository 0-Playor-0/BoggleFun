import basicui as bui
import wordPlay


foundPaths = []
foundWords = []
#Take input as z lines of code in the form (x,y) where x and y are coordinates and z is the number of letters in the word.

def algo():
    inputs = []
    
    inputs.append(input('First Letter ("x,y") :'))

    while True:
        inp = str(input('Next Letter ("x,y") and "No" to Exit :'))
        if inp == "Done" or inp == "done" or inp == "no" or inp == "No":
            break
        else:
            inputs.append(inp)

    workInputs = []
    
    for inp in inputs:
        i = []
        inp = inp.strip("")
        i = inp.split(",")
        for x in range (len(i)):
            i[x] = int(i[x])
        workInputs.append(i)
    
    checker(workInputs)
    print(workInputs)
    return None
#Things left to do : Check if the position given is possible on the board of n - _/
#Ensure that it is not possible to enter same location two times. - _/
#Make it so that unlimited tries on words - _/
#Ensure that the words are compared to the csv file to ensure that there is no funny business ocurring. - _/
#Ensure that points system is linked to the foundWords - _/
#Add a working timer later on
#Ensure the benefits of the same combination cannot be reaped more than once.

def checker(inputs):
    for inp in range (len(inputs)-1):
        if inp<len(inputs):
            if bui.n>=inputs[inp][0] and bui.n>=inputs[inp][1]:
                if (abs(inputs[inp][0]-inputs[inp+1][0])>1):
                    print("This move is not possible, go again")
                    algo()
                    return None
                else:
                    if (abs(inputs[inp][1]-inputs[inp+1][1])>1):
                        print("This move is not possible, go again")
                        algo()
                        return None
            else:
                print("One of what you have selected is out of the board. Please change it!")
                algo()
                return None
    
    for inp2 in inputs:
        same = 0
        for inp1 in inputs:
            if inp1[0] == inp2[0] and inp1[1] == inp2[1]:
                same+=1
    if same>1:
        print("There are repeats in the current list of coordinates, fix that please!")
        algo()
        return None

    word = ""    
    for inp in inputs:
        word+=bui.Grid[inp[0]][inp[1]]
    
    if inputs not in foundPaths:
        if wordPlay.checkEng(word.lower()):
            foundWords.append(word)
            foundPaths.append(inputs)
        else:
            return None
    else:
        print("You cannot reap the benefits of one path twice!!!")
        


    

                

