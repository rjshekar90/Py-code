"""
This is a Python file for creating
Markov Chains.

Because this string is at the top
of the file, it is a special string.
It is called a *docstring*.

>>> m = Markov('ab')
>>> m.predict('a')
'c'

>>> get_table('ab')
{'a': {'b': 1}}

"""

import random


class Markov:
    def __init__(self, data):
        self.table = get_table(data)

    def predict(self, data_in):
        options = self.table.get(data_in, {})
        if not options:
            raise KeyError()
        possible = ''
        for key, count in options.items():
            possible += key * count
        result = random.choice(possible)
        return result


def get_table(line):
    """This is a function docstring"""
    results = {}
    # loop over characters in line
    for i, c in enumerate(line):
        # get the character following the character
        try:
            out = line[i + 1]
        except IndexError:
            break
        # if we haven't seen the character
        # create a new inner dictionary
        char_dict = results.get(c, {})
        # insert following with count
        char_dict.setdefault(out, 0)
        # incremented by one
        char_dict[out] += 1
        # stick inner dictionary in outer
        results[c] = char_dict
    return results


if __name__ == '__main__':
    m = Markov('ab')
    import doctest
    doctest.testmod()