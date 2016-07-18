"""Source: https://www.hackerrank.com/challenges/swap-case
You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string .

Constraints


Output Format

Print the modified string .

Sample Input

HackerRank.com presents "Pythonist 2".
Sample Output

hACKERrANK.COM PRESENTS "pYTHONIST 2"."""


def main(s):
    return s.swapcase()


if __name__ == '__main__':
    s = raw_input()
    print main(s)
