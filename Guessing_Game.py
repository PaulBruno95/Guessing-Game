print("Welcome to the guessing game, you have three attempts to guess the right animal! \n Please see the 3 "
      "hints below:\n Hint #1: It is a spotted animal\n Hint #2: It has a very long tongue\n Hint #3: It is one of the "
      "tallest animals on Earth\nGOOD LUCK!")
secret_word = "giraffe" or "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while not (not (guess != secret_word) or out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("\n")
    print("Out of Guesses, YOU LOSE!\nCorrect Answer: giraffe")
else:
    print("\n")
    print("CONGRATULATIONS! YOU WIN!")
