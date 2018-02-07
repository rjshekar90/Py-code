
import time
from functools import wraps

def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """
    @wraps(some_function)
    def wrapper(*args, **kwargs):
        # t1 = time.time()
            return some_function(*args, **kwargs)
    print('Not executing decorated fn.')

    # return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function(x, y):
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))
    print(f'The values are {x} and {y}')


(my_function(3, 9))