import random

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

def start_game():
    print("Hello traveler! Welcome to the game of guesses!")

    player_name = input("What is your name? ")
    wanna_play = input(f"Hi, {player_name}, would you like to play the guessing game? (Enter Yes/No) ")

    show_score()

    while wanna_play.lower() == "yes":
        random_number = random.randint(1, 10)
        
        attempts = 0

        while True:
            try:
                guess = int(input("Pick a number between 1 and 10: "))
                

                if guess < 1 or guess > 10:
                    raise ValueError("Please guess a number within the given range (1-10).")
                
                attempts += 1

                if guess == random_number:
                    print("Nice! You got it!")
                    attempts_list.append(attempts)
                    print(f"It took you {attempts} attempts.")
                    break
                elif guess > random_number:
                    print("It's lower")
                else:
                    print("It's higher")

            except ValueError as err:
                print("Oh no! That is not a valid value. Try again...")
                print(f"({err})")

        wanna_play = input("Would you like to play again? (Enter Yes/No) ")
        if wanna_play.lower() != "yes":
            print("That's cool, have a good one!")
            break
        else:
            show_score()

if __name__ == '__main__':
    start_game()
