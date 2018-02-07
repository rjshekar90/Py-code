# !/usr/bin/env python
#
# def print_log(func):
#     def wrapper(*arg, **kwargs):
#         print('Calling: ' + func.__name__)
#         return func(*arg, **kwargs)
#
#     return wrapper
#
#
# @print_log
# def f(n, m):
#     return n + m + 12
#
#
# print(f(5, 5))
#
from functools import wraps
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('exec b4 dec')
#         func(*args, **kwargs)
#         print('after the dec')
#     return wrapper
#
# @my_decorator
# def add_no(x, y):
#     print(x+y)
#
# (add_no(9, 10))


#
# def decorator_with_args(num):
#     def my_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print('in the dec')
#             if num == 56:
#                 print('num is 56')
#             else:
#                 func(*args, **kwargs)
#             print('exiting the dec')
#         return wrapper
#     return my_decorator
#
#
#
# @decorator_with_args(59)
# def my_fn_too(nope, nopee):
#     print(nope, end='\n')
#     print(nopee)
#
# my_fn_too('hello', 'world')



# memoization
# import time
#
# def f(*args):
#     print(args)
#     time.sleep(2)
#     print(args)
# cache = {}
# def cached_fn(*args):
#     key = (args)
#     if key not in cache:
#         cache[key] = f(args)
#     return cache[key]
#
# cached_fn(2,3,2,45)

# def memoize(func):
#     memory = dict()
#     def wrapper(*args):
#         if args not in memory:
#             memory[args] = func(*args)
#         return memory[args]
#     return wrapper
#
#
#
# @memoize
# def f(x):
#     print("CALLING: f {}".format(x))
#     return x ** 2
#
# @memoize
# def g(x, y):
#     print("CALLING: g {} {}".format(x, y))
#     return (2 - x) / y
#
# print(f(10))
#
# print(g(10, 3))
#
# print(f(10))
#



