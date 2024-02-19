import random
 
words = ['coding', 'class', 'united', 'manchester',
         'sleep', 'math', 'salamander', 'oblidge',
         'wet', 'people', 'bolder', 'boat']
 
word = random.choice(words)
 
 
print("Guess the characters")
 
guesses = ''
 
turns = 8
 
 
while turns > 0:
 
    failed = 0
 
    for character in word:
 
        if character in guesses:
            print(character, end=" ")
 
        else:
            print("_")
 
            failed += 1
 
    if failed == 0:

        print("You Win")
 
        print("The word is: ", word)
        break
 
    print()
    guess = input("guess a character:")
 
    guesses += guess
 
    if guess not in word:
 
        turns -= 1
 
        print("Wrong")

        print("You have", + turns, 'more guesses')
 
        if turns == 0:
            print("You Loose")