"""
TASK 1: Hangman Game
CodeAlpha Python Internship
Author: JP
"""

import random

# ── Word bank ──────────────────────────────────────────────────
WORDS = ["python", "circuit", "voltage", "network", "binary"]

# ── Visual stages (6 wrong guesses allowed) ───────────────────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

def display_state(word, guessed, wrong_count):
    """Print current game state."""
    print(HANGMAN_STAGES[wrong_count])
    # Show word progress: e.g.  _ y _ _ _ _
    display = " ".join(ch if ch in guessed else "_" for ch in word)
    print(f"\n  Word: {display}")
    print(f"  Wrong guesses left: {6 - wrong_count}")
    wrong_letters = [ch for ch in guessed if ch not in word]
    if wrong_letters:
        print(f"  Incorrect letters: {', '.join(sorted(wrong_letters))}")

def hangman():
    word = random.choice(WORDS)
    guessed = set()
    wrong_count = 0
    max_wrong = 6

    print("\n" + "="*40)
    print("       Welcome to HANGMAN!")
    print("="*40)
    print(f"  The word has {len(word)} letters. Good luck!\n")

    while wrong_count < max_wrong:
        display_state(word, guessed, wrong_count)

        # Check win
        if all(ch in guessed for ch in word):
            print(f"\n  🎉 You won! The word was: '{word.upper()}'")
            break

        # Get valid input
        while True:
            guess = input("\n  Guess a letter: ").strip().lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed:
                    print("  You already guessed that letter. Try another.")
                else:
                    break
            else:
                print("  Please enter a single letter.")

        guessed.add(guess)

        if guess in word:
            print(f"  ✅ '{guess}' is in the word!")
        else:
            wrong_count += 1
            print(f"  ❌ '{guess}' is NOT in the word.")

    else:
        # Ran out of guesses
        display_state(word, guessed, wrong_count)
        print(f"\n  💀 Game over! The word was: '{word.upper()}'")

    play_again = input("\n  Play again? (y/n): ").strip().lower()
    if play_again == "y":
        hangman()
    else:
        print("\n  Thanks for playing Hangman! Goodbye.\n")

if __name__ == "__main__":
    hangman()
 Hangman Game - Task 1
# Add your code here

