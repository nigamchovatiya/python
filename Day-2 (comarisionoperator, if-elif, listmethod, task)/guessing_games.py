# import random


def game_random(attempts: int, a: int, b: int) -> None:
    """
         number guessing game with limited attempts

         Args :
                attempts (int) : Total attempts for user
                a (int) : starting range for number to guess
                b (int) : Ending range for number to guess

         Returns :
                None : it prints user is win or loose.

    """

    # n = random.randint(a,b) # random generate a number
    n = 8  # mannual given number

    while (attempts > 0):
        user_number = int(input(f"\nGuess a Number Between {a} and {b} : "))
        if (n == user_number):
            print("You Won")
            break
        else:
            attempts -= 1  # attempts = attempts - 1
            print("You guess was incorrect ! Try Again")
            print(f"No. of attempts left - {attempts}")
            print(" \n " * attempts)

    if attempts == 0:
        print("Oops ! You Lose the Game")


game_random(3, 1, 10)
