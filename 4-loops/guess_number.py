# Guess Number 🔢
# Codédex

guess = 0
tries = 0

while guess != 6 and tries < 5 :
    guess = int(input("Guess the number:  "))
    tries += 1
    if guess == 6:
        print('You Got it!')
        
if tries == 5:
    print("You ran out of tries :(")

