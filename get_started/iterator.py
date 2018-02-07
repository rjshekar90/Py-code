
class fib:
    def __init__(self, limit = None):
        self.val1 = 1
        self.val2 = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        val = self.val1
        self.val1 = self.val2
        self.val2 = val + self.val1
        if self.limit is not None and \
            val < self.limit:
            return val
        raise StopIteration






e = fib(2)
# for val in e:
#     print(val)

it = iter(e)
print(next(it))

print(next(it))

#print(next(it))