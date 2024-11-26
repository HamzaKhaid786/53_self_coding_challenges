"""Ask the user for a number and print its square (the product of the number times itself)."""

def main():
    print("Number Squared")
    num : float = float(input("Type a number to see its square: "))
    square : float = num**2
    print(f"{num} squared is {square}")



if __name__ == '__main__':
    main()