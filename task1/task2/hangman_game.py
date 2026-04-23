import random

words = ["apple", "tiger", "chair", "plant", "river"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    
    display = ""
    
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    
    print("\nWord:", display)
    
    if display == word:
        print("Congratulations! You guessed the word.")
        break
    
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
    
    elif guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)
    
    else:
        print("Wrong guess!")
        wrong_guesses += 1
        guessed_letters.append(guess)
        print("Remaining attempts:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("Game Over! The word was:", word)
