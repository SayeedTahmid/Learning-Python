import random

LOW = 100
HIGH = 200
MAX_ATTEMPTS = 3
keep_playing = True

while keep_playing:
    set_num = random.randint(LOW, HIGH)
    attempts_left = MAX_ATTEMPTS
    has_won = False

    while attempts_left > 0 and not has_won:
        while True:
            try:
                guess_num = int(input(f"Enter a number from {LOW}-{HIGH}: "))
                if LOW <= guess_num <= HIGH:
                    break
                print(f"Number must be {LOW}-{HIGH} only")

            except ValueError:
                print("Not a number")

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
