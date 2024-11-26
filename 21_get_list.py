"""Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list."""

def main():
    my_list = []  

    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input isn't an empty value
        my_list.append(val) # Add val to list
        val = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", my_list)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()