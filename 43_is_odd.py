"""Filter out even and odd number in a given range"""
def main():
    for i in range(21):
        if is_odd(i):
            print(f'{i} odd')
        else:
            print(f'{i} even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2  
    return remainder 


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()