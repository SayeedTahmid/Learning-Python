import random

LOW = 100
HIGH = 200
MAX_ATTEMPTS = 3
keep_playing = True

def get_valid_guess(low, high):
    while True:
        try:
            guess= int(input(f"Enter a number from {low}-{high}: "))
            if low <= guess <= high:
                 return guess
            print (f"Number must be {low}-{high}")
        except ValueError:
            print("Not a number")

while keep_playing:
    set_num = random.randint(LOW, HIGH)
    attempts_left = MAX_ATTEMPTS
    has_won = False

    while attempts_left > 0 and not has_won:

        guess_num = get_valid_guess(LOW, HIGH)

        attempts_left -= 1

        if guess_num == set_num:
            print("Correct")
            has_won = True
        elif guess_num > set_num:
            print("high")

        else:
            print("low")

        print(f"{attempts_left} left")

    if not has_won:
        print("correct num", set_num)

    answer = input("Play Again ? y/n: ")
    keep_playing = answer.lower() == "y"
