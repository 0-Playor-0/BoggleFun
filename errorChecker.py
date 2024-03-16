import algo 
import basicui as bui
import wordPlay


def checker(inputs):
    for inp in range (len(inputs)-1):
        if inp<len(inputs):
            if bui.n>=inputs[inp][0] and bui.n>=inputs[inp][1]:
                if (abs(inputs[inp][0]-inputs[inp+1][0])>1):
                    print("This move is not possible, go again")
                    algo.algo()
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
    
    for inputPrimary in inputs:
        RepeatedCoordinates = 0
        for inputSecondary in inputs:
            if inputSecondary[0] == inputPrimary[0] and inputSecondary[1] == inputPrimary[1]:
                RepeatedCoordinates+=1
    if RepeatedCoordinates>1:
        print("There are repeats in the current list of coordinates, fix that please!")
        algo()
        return None

    word = ""    
    for input in inputs:
        word+=bui.Grid[input[0]][input[1]]
    
    if inputs not in algo.foundPaths:
        if wordPlay.checkifEngWord(word.lower()):
            algo.foundWords.append(word)
            algo.foundPaths.append(inputs)
        else:
            return None
    else:
        print("You cannot reap the benefits of one path twice!!!")
        