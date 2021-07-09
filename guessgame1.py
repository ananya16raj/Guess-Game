import random
name = input("What's your name? ")
print("Good Luck !", name)
words = ['rainbow', 'computer','biology','physics','chemistry','maths','water','railway','travel','winter']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 10
while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_", sep =',')
            failed = failed + 1
    if(failed == 0):
        print("You Win")
        print("The word is:",word)
        break;
    guess  = input("Guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
        print("By far you have made guesses: ", guesses)


        if(turns == 0):
            print("You loose")
            print("The word was", word)
