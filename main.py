import random

IF_HIGH = "Too high."
IF_LOW = "Too low."
IF_CORRECT = "You've got it!"


def set_difficulty():
   while True:
       mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
       if mode in ["easy", "hard"]:
           return 10 if mode == "easy" else 5  # Return the number of lives
       print("Invalid input. Please choose 'easy' or 'hard'.")


def main():
   while True:
       life = set_difficulty()  # Set life based on difficulty
       CORRECT_GUESS = random.randint(1, 100)

       # Include ASCII art logo here (optional)

       while life > 0:  # Continue as long as there are lives remaining
           user_guess = int(input("Guess a number between 1 and 100: "))
           check_guess(user_guess, CORRECT_GUESS, life)
           if user_guess == CORRECT_GUESS:
               break  # Correct guess, exit the loop

       if life == 0:
           print("You've run out of guesses, you lose.")
       else:
           print(f"{IF_CORRECT}, the correct answer is {CORRECT_GUESS}")

       play_again = input("\nDo you want to play again? (yes/no): ").lower()
       if play_again != "yes":
           break

   print("Goodbye.")


def check_guess(user_guess, correct_guess, life):
   if user_guess > correct_guess:
       print(IF_HIGH)
   elif user_guess < correct_guess:
       print(IF_LOW)
   else:
       return  # Correct guess, exit the function
   life -= 1  # Decrement life for incorrect guesses
   print(f"You have {life} attempts remaining to guess the number.")


if __name__ == "__main__":
   main()
