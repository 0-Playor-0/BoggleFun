

def calculate_total(words):
    points = 0
    for word in words:
        points += len(word)
    print("Your score is" , points , "!")