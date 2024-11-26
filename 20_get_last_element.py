"""Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length."""
def get_last_element(lst):
    """print the first element of a list"""
    print(lst[-1])

def get_list():
    """Prompts user to enter elements of list one at a time and return the resulting list"""
    lst=[]
    elem: str = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst


def main():
    lst = get_list()
    get_last_element(lst)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()