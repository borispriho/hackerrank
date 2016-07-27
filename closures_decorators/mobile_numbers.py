"""Source: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators
Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer , the number of mobile phone numbers.
 lines follow each containing a mobile number.

Output Format

Print  mobile numbers on separate lines in the required format.

Sample Input

> 3
> 07895462130
> 919875641230
> 9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230
Concept

Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps here.
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function."""


class Mobiler(list):
    '''A class wrapping a list of mobile phones sanising it's format'''

    def __init__(self, values=None):
        self.values = values or []

    def __str__(self):
        return '\n'.join(self.values)

    def wrap_number(func):
        PREFIX = '+91'
        DIGITS = 10

        def wrapper(self, value):
            number = value[-DIGITS:]
            value = '%s %s %s' % (PREFIX, number[:5], number[5:])
            res = func(self, value)
            self.values = sorted(self.values)
            return res
        return wrapper

    @wrap_number
    def append(self, value):
        self.values.append(value)


def main():
    mobiler = Mobiler()
    phones_count = raw_input()  # Enter the phones number
    assert phones_count.isdigit(), "You've entered not a number, exiting."

    for i in xrange(int(phones_count)):
        phone = raw_input()  # Enter  the phone
        mobiler.append(phone)
    print str(mobiler)

if __name__ == '__main__':
    main()
