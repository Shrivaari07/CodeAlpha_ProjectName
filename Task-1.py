import random
a=["project","apple","python","beginner","internship"]
word=random.choice(a)
guessed_letter=[]
wrong_guess=0
max_wrong=6
print("-----HANGMAN GAME-----")
while wrong_guess < max_wrong:
    display=""
    for letter in word:
        if letter in guessed_letter:
            display=display+letter+" "
        else:
            display=display+"_ "
    print("\nWord:",display)
    if "_" not in display:
        print("hurry! YOU WON")
        break
    guess=input("Enter a Letter:").lower()
    if len(guess)!=1:
        print("You already guessed this letter.")
        continue
    guessed_letter.append(guess)
    if guess in word:
        print("Correct")
    else:
        wrong_guess=wrong_guess+1
        print("Wrong")
        print("Remaining chances:",max_wrong-wrong_guess)
        if wrong_guess==max_wrong:
            print("\nYOU LOST")
            print("The word is: ",word)    