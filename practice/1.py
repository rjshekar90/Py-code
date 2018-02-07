# def take_args(*args):
#     """
#
#     :rtype: values
#     """
#     for arg in args:
#         print(arg)
#
#
#
# take_args(1 ,2 ,3 ,4)

#
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}---->{value}')
#
#
# print_kwargs(name='Raj')

#
# def add_to_dict(stuff, **kwargs):
#     for key, value in kwargs.items():
#         if key not in stuff:
#             stuff[key] = value
#     return stuff
#
# print(add_to_dict(dict(foo=1), foo='1', hello='3'))


# def normal_numbers(a, b, c):
#     print(f'a:{a}, b:{b}, c:{c}')
#
# nos = 1,2,3
#
# normal_numbers(*nos)


# def key_for_biggest_value(**values):
#     rk, rv = None, None
#     for key, value in values.items():
#         if rk is None or value>rv:
#             rk, rv = key, value
#     print(rk)
#
# key_for_biggest_value(foo=10, alpha=3, x=9)

#
# def max_int_values(lst):
#     biggest = abs(lst[0])
#     print(biggest)
#     for num in lst[1:]:
#         num = abs(num)
#         if num > biggest:
#             biggest = num
#
#     return biggest
#
#
# print(max_int_values([-100, -9, 3, -200]))

#
# def max_by_key(items, key):
#     biggest = items[0]
#     for item in items:
#         if key(item) > key(biggest):
#             biggest = key(item)
#     return biggest
#
#
# print(max_by_key([2,3,-6,1], abs))
#
# def return_gpa(students, gop, val):
#     rk, rv = None, None
#     for k, v in students.items():
#
#         if rk is None or gop(v) > val:
#             rk, rv = k, v
#     return rk, rv
#
#
# print(return_gpa(dict(hello='1', name='9', raj='2'), int, 3))

#
# student_joe = {'gpa': 3.7, 'major': 'physics',
#                'name': 'Joe Smith'}
# student_jane = {'gpa': 3.8, 'major': 'chemistry',
#                 'name': 'Jane Jones'}
# student_zoe = {'gpa': 3.4, 'major': 'literature',
#                'name': 'Zoe Grimwald'}
# students = [student_joe, student_jane, student_zoe]
#
#
# def get_gpa(who):
#     return who['gpa']
#
#
# print(sorted(students, key=get_gpa))

#
# one_line_poems = [
#    "The dogs are barking at the stillness, the stillness is still.",
#   "In the canopy of the night heaven the stars are tiptoeing.",
#     "A sunrise smiles wide into my expectant face.",
#    "The bees are awakening to the life in a yellow wonder!",
#    "The land runs astoundingly under my soles.",
#    "The dance of the flowers kissed by the butterflies.",
# ]
#
# def fewest_vowels(inp):
#     def count_vowels(s):
#         return s.count('aeiou')
#     return max(one_line_poems, key=count_vowels)
#
# print(fewest_vowels(one_line_poems))

# def count_char(s, subset):
#
#     count = 1
#     for c in s.lower():
#         if c in subset:
#             count+=1
#     return count
#









