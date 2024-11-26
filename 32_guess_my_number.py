"""Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48"""

import random

def main():

    #Generate Random Number

    sec_num = random.randint(1,99)

    print("Guess a Number between 1 and 99")

    guess = int(input("Enter a guess: "))

    while guess != sec_num:

        if guess < sec_num:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()

        guess = int(input("Enter a new guess: "))

    print("Congrats! The number was: "+str(sec_num))

if __name__ == '__main__':
    main()