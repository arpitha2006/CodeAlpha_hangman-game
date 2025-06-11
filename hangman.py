import random

def hangman_game():
    words = ["python", "computer", "programming", "coding", "software"]
    
    word = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    prefilled_letter = random.choice(word)
    guessed_letters.append(prefilled_letter)
    
    print("Welcome to Hangman Game!")
    print(f"Word has {len(word)} letters")
    
    display_word = ""
    for letter in word:
        if letter == prefilled_letter:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"Starting word: {display_word}")
    
    while incorrect_guesses < max_incorrect:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nCurrent word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {word.upper()}")
            return
        
        guess = input("\nEnter a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            
            if incorrect_guesses >= 3:
                print(f"Hint: This word is related to technology and programming.")
    
    print(f"\nGame Over! The word was: {word.upper()}")

def main():
    while True:
        hangman_game()
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again != 'y' and play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()