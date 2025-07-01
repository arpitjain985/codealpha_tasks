import random

def hangman():
    words = ['python', 'hangman', 'computer', 'programming', 'keyboard']

    secret_word = random.choice(words)
    
    guessed_letters = ['_'] * len(secret_word)
    
    guessed_set = set()
    
    max_attempts = 6
    incorrect_guesses = 0
    
    print("Welcome to Hangman!")
    print(" ".join(guessed_letters))
    
    while True:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
    
        if guess in guessed_set:
            print("You already guessed that letter.")
            continue
        
        guessed_set.add(guess)
        
        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_letters[i] = guess
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_attempts - incorrect_guesses} attempts left.")
        
        print(" ".join(guessed_letters))
        
        if "_" not in guessed_letters:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
        
        if incorrect_guesses >= max_attempts:
            print(f"Game over! The word was: {secret_word}")
            break

hangman()
