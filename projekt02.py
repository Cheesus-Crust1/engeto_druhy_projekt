from random import sample
from time import time


print(
    "Hi there!", ODD := "=" * 47,
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.", ODD, sep="\n"
)

while True:
    cislo = sample(range(10), 4)
    if cislo[0] != 0:
        break

pocitadlo = int()
start = time()

while True:
    while True:
        if (tip := input("Enter a number:")).isdecimal() \
                and len(tip) == 4 \
                and (len(set(tip))) == len(tip) \
                and tip[0] != '0':
            tip = list(map(int, tip))
            pocitadlo += 1
            break
        else:
            print(
                "Wrong input, please enter only 4"
                " digit number with unique digits."
            )
    if tip == cislo:
        if pocitadlo > 1:
            print(
                ODD, "Correct, you've guessed the right number",
                f"in {pocitadlo} guesses!", sep='\n'
            )
        else:
            print(
                ODD, "Correct, you've guessed the right number",
                f"in {pocitadlo} guess!", sep='\n'
            )
        end = time()
        print(f"Your time {round(end - start, 2)}", ODD, sep="\n")
        break
    elif set(tip).intersection(set(cislo)):
        bulls = 0
        cows = 0
        for index in range(0, 4):
            if tip[index] == cislo[index]:
                bulls += 1
            elif tip[index] in cislo:
                cows += 1
        if bulls > 1:
            print(f"{bulls} bulls", end=" ")
        else:
            print(f"{bulls} bull", end=" ")
        if cows > 1:
            print(f"{cows} cows")
        else:
            print(f"{cows} cow")
        print(ODD)
