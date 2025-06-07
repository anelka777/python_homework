def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)

        displayed_word = ''.join([char if char in guesses else '_' for char in secret_word])
        print(displayed_word)

        return all(char in guesses for char in secret_word)    
    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ").lower()
    hangman = make_hangman(secret)

    print("\nStart guessing the letters!")

    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        done = hangman(guess)
        if done:
            print("Congratulations! You guessed the word!")
            break