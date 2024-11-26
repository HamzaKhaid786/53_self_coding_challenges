"""Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

There are 5 seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute."""


DAYS_PER_YEAR : int = 365
HOURS_PER_DAY : int = 24
MIN_PER_HOUR : int = 60
SEC_PER_MIN : int = 60


def main():
    print("Seconds in a Year")
    seconds_in_a_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    print(f"There are {seconds_in_a_year}  seconds in a year!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()