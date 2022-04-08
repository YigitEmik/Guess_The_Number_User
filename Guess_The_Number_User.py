import random
def guess(x):
    low = 1
    high = x + 1
    feedback = " "
    attempt = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? :").lower()
        attempt += 1
        if feedback == 'l'.lower():
            low = guess + 1
        elif feedback == 'h'.lower():
            high = guess - 1
        elif feedback == 'c'.lower():
            print(f"Nice, I won! The number was {guess} and I found this in {attempt} attempts!")
guess(100)
            
    