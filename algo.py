import basicui as bui
import wordPlay
import errorChecker
import sys
import time
  
global timerOld
global half
global one
global oneHalf
global two

timerOld = time.time()
#The foundPaths is where all paths are stored to ensure repeats are not allowed, and similarly foundWords help to calculate the points!

foundPaths = []
foundWords = []
half = False
one = False
oneHalf = False
two = False

#Take input as z lines of code in the form (x,y) where x and y are coordinates and z is the number of letters in the word.

def algo():
    inputs = []    

    firstInput = str(input("First Letter (x,y) :"))
    if firstInput == "exit" or firstInput == "Exit":
        sys.exit("You exitted the game")
    inputs.append(firstInput)
    
    secondInput = input("Second Letter (x,y) :")
    if secondInput == "exit" or firstInput == "Exit":
        sys.exit("You exitted the game")
    inputs.append(secondInput)

    while True:
        #Timer Doesnt work yet due to various errors.
        """
        if timerOld + 120 < time.time() and two == False:
            print("\nYour time has passed, sorry!\n")
            two = True
            return None
        elif timerOld + 90 < time.time() and oneHalf == False:
            print("\n1.5 minutes have passed\n")
            oneHalf = True
        elif timerOld + 60 < time.time() and one == False:
            print("\n1 minute has passed\n")
            one = True
        elif timerOld + 30 < time.time() and half == False:
            print("\n30 seconds have passed\n")
            half = False
            return None
        """
        Input = str(input('Next Letter ("x,y") and "No" to Exit :'))
        if Input == "Done" or Input == "done" or Input == "no" or Input == "No":
            break
        else:
            inputs.append(Input)

    workInputs = []
    try:
        for Input in inputs:
            i = []
            Input = Input.strip("")
            i = Input.split(",")
            for x in range (len(i)):
                i[x] = int(i[x])
            workInputs.append(i)
    
        errorChecker.checker(workInputs)
        print(workInputs)
    except:
        print("Since something went wrong! Make sure all your entries are in the right format and there are atleast 3 letters in the word")
    return None

#Things left to do : Check if the position given is possible on the board of n - _/
#Ensure that it is not possible to enter same location two times. - _/
#Make it so that unlimited tries on words - _/
#Ensure that the words are compared to the csv file to ensure that there is no funny business ocurring. - _/
#Ensure that points system is linked to the foundWords - _/
#Add a working timer later on
#Ensure the benefits of the same combination cannot be reaped more than once.




    

                

