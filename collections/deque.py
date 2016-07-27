#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
"""

from collections import deque


if __name__ == '__main__':
    methods_num = raw_input()
    d = deque()
    for i in xrange(int(methods_num)):
        args = None
        user_input = raw_input().split()
        method_name = user_input[0]
        if len(user_input) > 1:
            method_name, args = user_input
            getattr(d, method_name)(args)
        else:
            getattr(d, method_name)()
    print ' '.join(list(d))
