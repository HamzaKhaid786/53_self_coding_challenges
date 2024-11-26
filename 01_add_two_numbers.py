'''Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.

Print the total sum with an appropriate message.'''


def main():
    num1 = input("Enter first number: ")
    n1 = int(num1)
    num2 = input("Enter second number: ")
    n2 = int(num2)
    total = n1 + n2
    print("The total is " ,total, ".")



if __name__ == '__main__':
    main()