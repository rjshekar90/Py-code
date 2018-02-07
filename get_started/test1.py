#
# class Person:
#
#     def __init__(self):
#         self._name = None
#
#     @property
#     def name(self):
#         if self._name == 'Richard':
#             return 'Ringo'
#         return self._name
#
#     @name.setter
#     def set_name(self, value):
#         self._name = value
#
#     @name.deleter
#     def del_name(self):
#         del self._name
#
# p = Person()
# print(p.name)

names = ['james', 'thames', 'raj']

# for name in names:
#     if name == 'raj':
#         break
#     print(name)
#
# for name in names:
#     if name == 'thames':
#         continue
#     print(name)

#
# for i, v in enumerate(names, 1):
#     print(f'{i} ---- {v}')


# done = False
# while not done:
#     print('raj')
#     done = True

# ops = dict(plus = 'add')
# op = 'plus'
# a = 2
# b = 3
#
# print(ops[op])(a,b)

# try:
#     name='hello'
# except:
#     raise ValueError
# else:
#     print(name)
# finally:
#     name = 'raj'
#     print(name)


# def bark_dog(cls):
#
#     def bark(self):
#         return 'Woof Woof'
#     cls.barker = bark
#     return cls
#
# @bark_dog
# class Dog:
#     pass
#
# b = Dog()
# print(b.barker())

w = 'hello world'
for i, c in enumerate(w):
    if c != " ":
        print(i, c)
    else:
        break
