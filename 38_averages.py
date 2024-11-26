"""Write a function that takes two numbers and finds the average between the two."""

def average_calculator(a,b):
    average = (a+b)/2
    return average

def main():
    
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))

    average = average_calculator(x,y)

    print(f"The average od {x} and {y} is {average}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()