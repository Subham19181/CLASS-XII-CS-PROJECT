#Program 30

import random

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def word_guessing_game():
    words = ["python", "developer", "programming", "algorithm", "game", "software", "debugging", "string"]
    
    score = 0
    rounds = 5 
    
    print("Welcome to the Word Guessing Game!")
    
    for round_num in range(1, rounds + 1):
        original_word = random.choice(words)
        
        scrambled_word = scramble_word(original_word)
        
        print(f"\nRound {round_num}")
        print(f"Scrambled word: {scrambled_word}")
        
        guess = input("Guess the original word: ").strip().lower()
        
        if guess == original_word:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Oops! The correct word was '{original_word}'. You lost a point.")
            score -= 1
        
        print(f"Your current score: {score}")
    
    print("\nGame Over!")
    print(f"Your final score: {score}")

def main():
    word_guessing_game()

if __name__ == "__main__":
    main()