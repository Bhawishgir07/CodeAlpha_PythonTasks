import random

def hangman():
    words = ["python", "codealpha", "developer", "script", "program"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("--- Welcome to Hangman Game ---")
    
    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord:", display_word.strip())
        print(f"Remaining attempts: {attempts}")
        
        if "_" not in display_word:
            print("\nCongratulations! Aap jeet gaye! Word tha:", secret_word)
            break
            
        guess = input("Ek letter guess kijiye: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Kripya sirf ek valid letter enter karein.")
            continue
            
        if guess in guessed_letters:
            print("Aapne ye letter pehle hi guess kar liya hai.")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"Sahi jawab! '{guess}' word mein hai.")
        else:
            print(f"Galat jawab! '{guess}' word mein nahi hai.")
            attempts -= 1
            
    if attempts == 0:
        print("\nGame Over! Aapke saare attempts khatam ho gaye. Word tha:", secret_word)

if __name__ == "__main__":
    hangman()