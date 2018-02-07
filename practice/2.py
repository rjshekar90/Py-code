__author__ = ""
__copyright__ = ""


# !/usr/bin/env python
# Property defined

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return self.first_name + " " + self.last_name
#
#
# person = Person('Raja', 'Shekar')
# print(person.full_name)


def print_log(func):
    def wrapper(arg):
        print('Calling: ' + func.__name__)
        return func(arg)
    return wrapper

@print_log
def g(n):
    return n+5

@print_log
def h(n):
    return n+9

print(g(2))

print(h(5))