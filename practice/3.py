#
#
# def apply(fn, val):
#     return fn(val)
#
# apply(print, 5)

def outer():
    def inner():
        print('invoking this returns the inner')
        def hello():
            print('hello')
    #print('invoking this is the outer')
        hello()

print(outer())