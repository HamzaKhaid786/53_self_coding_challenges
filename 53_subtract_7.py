"""Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function!"""
def main():
    num = 7  # Declare and initialize the variable properly
    num = subtract_seven(num)  # Call the subtract_seven helper function
    print("this should be zero: ", num)

def subtract_seven(num):
    num = num - 7  # Subtract 7 from num
    return num  # Return the updated value

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
