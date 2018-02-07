#!/usr/bin/env python

__author__ = " "
__copyright__ = " "

"""
Markov Chain Class design

>>> m = Markov('ab')
>>> m.predict('a')
'b'

>>> get_table('ab')
{'a':{'b':1}}
"""


class Markov:
    """ Markov constructor"""

    def __init__(self, data):
        self.table = None

    def predict(self, data_in):
        return 'b'

def get_table(line):
    """This is a fn. docstring"""
    results = dict()
    # loop over chars in a line
    for i, c in enumerate(line):
        # get the chars following ith one
        try:
            out = line[i+1]
        except IndexError:
            break
        # if we haven't seen the char
        # create the new inner dict
        char_dict = results.get(c, {})
        # insert the following with count
        char_dict.setdefault(out, 0)
        # increment the value
        char_dict[out] += 1
        # stick the inner dict to outer dict
        results[c] = char_dict
    return results
















if __name__ == '__main__':
    m = Markov('ab')
    print(m.predict('a'))
    print(get_table('abcbs'))



