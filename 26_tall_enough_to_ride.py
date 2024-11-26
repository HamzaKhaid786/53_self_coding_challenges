"""Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

Here's two sample runs (user input is in bold italics):

How tall are you? 100

You're tall enough to ride!

How tall are you? 10

You're not tall enough to ride, but maybe next year!

"""

MINIMUM_HEIGHT = 50  # arbitrary units :)

def main():
    while True:  # Loop until the user exits
        user_input = input("How tall are you? ")
        if user_input == "":  # Exit if no input is provided
            print("Exiting the program. Goodbye!")
            break
        
        try:
            height = float(user_input)  # Attempt to convert input to a float
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Invalid input! Please enter a valid height or press Enter to exit.")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
