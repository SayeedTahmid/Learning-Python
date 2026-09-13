import random

keep_playing = True

while keep_playing:
    set_num = random.randint(1, 100)
    attempts_left = 5
    has_won = False

    while attempts_left > 0 and not has_won:
        while True:
            try:
                guess_num = int(input("Enter a number from 1-100: "))
                if 1 <= guess_num <= 100:
                    break
                print("Number must be 1 to 100 only")

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

        print("attempts left = ", attempts_left)

    if not has_won:
        print("correct num", set_num)

    answer = str(input("Play Again ? y/n: "))
    keep_playing = answer.lower() == "y"
