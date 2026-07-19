def calculate_total(words):
    total = sum(len(word) for word in words)
    print(f"Your score is {total}!")
    return total
