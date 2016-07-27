#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:

Mr. Henry Davids
For Mary George, the output should be:

Ms. Mary George
Input Format

The first line contains the integer , the number of people.
 lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Constraints


Output Format

Output  names on separate lines in the format described above in ascending order of age."""


class Person(object):
    REFS = ('name', 'surname', 'age', 'sex')

    def __init__(self, description):
        for ref, val in zip(self.REFS, description.split()):
            setattr(self, ref, val)

    def __str__(self):
        return ' '.join([self.name, self.surname])


class PolitePerson(Person):
    """Class representing polite Person's form"""

    def unify(func):
        def add_title(self):
            res = func(self)
            title = 'Mr.' if self.sex == 'M' else 'Ms.'
            setattr(self, 'title', title)
            return ' '.join([title, res])
        return add_title

    @unify
    def __str__(self):
        return super(PolitePerson, self).__str__()


class PersonContainer(list):
    """Generic container for holding Person object's"""
    def get_persons(self):
        return sorted(list(self), key=lambda x: x.age)

    def __str__(self):
        persons = self.get_persons()
        return '\n'.join(map(str, persons))


def main():
    people = raw_input()
    container = PersonContainer()
    for i in xrange(int(people)):
        person = raw_input()
        container.append(PolitePerson(person))
    print str(container)

if __name__ == '__main__':
    main()
