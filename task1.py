import random

def choose_word():
    # These are the random words from which user can guess
    words = ['code', 'alpha', 'internship', 'python', 'programming','hangman','game']
    return random.choice(words)

def display_word(word, guessed_letters):
    
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 5
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
            return
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        # Check if the player has guessed all letters in the word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nYou've run out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()
