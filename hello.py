#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: guess_game.py
Description: Number guessing game - teaches you about input handling and loops
"""

import random

def guess_number():
    """Main game function"""
    
    print("\n" + "=" * 50)
    print("🎮 Number Guessing Game")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100")
    print("Try to guess it in as few attempts as possible!")
    
    # Secret number
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            # User input
            guess = input("\nEnter your guess (or 'quit' to exit): ")
            
            # Check for quit
            if guess.lower() in ['quit', 'exit', 'q']:
                print(f"The secret number was: {secret_number}")
                print("Thanks for playing! 👋")
                return
            
            # Convert input to number
            guess = int(guess)
            attempts += 1
            
            # Validate guess
            if guess < 1 or guess > 100:
                print("⚠️ Number out of range! Please enter a number between 1 and 100")
                continue
                
            if guess < secret_number:
                print("📈 Too low...")
            elif guess > secret_number:
                print("📉 Too high...")
            else:
                guessed = True
                print(f"\n🎉 Correct! The number was {secret_number}")
                print(f"✨ Number of attempts: {attempts}")
                
                # Performance rating
                if attempts <= 3:
                    print("🏆 Excellent! You're a pro!")
                elif attempts <= 7:
                    print("👍 Good job! But you can do better")
                else:
                    print("💪 Keep practicing!")
                    
        except ValueError:
            print("❌ Error: Please enter a valid number")
    
    print("=" * 50 + "\n")

def main():
    """Main function to run the game"""
    # Run the game
    guess_number()
    
    # Ask to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() in ['yes', 'y']:
            guess_number()
        else:
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()