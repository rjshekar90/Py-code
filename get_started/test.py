#
#
# add = lambda x, y: x+y
#
# print(add(10, 9))

# def add_kwargs(**kwargs):
#
#     result = 0
#     for _, value in kwargs.items():
#         if value:
#             result += value
#         else:
#             result += 0
#     return result
#
#
# print(add_kwargs(x=1, y=2, z=3))


class Bike:
    ''' Repr a bike'''
    num_passengers = 1

    def __init__(self, wheel_size, gear_ratio):
        ''' bike creation'''
        self.wheel_size = wheel_size
        self.gear_ratio = gear_ratio

    def gear_inches(self):
        return self.wheel_size * self.gear_ratio


class Tandem(Bike):
    ''' Inherited  a class'''

    def __init__(self, wheel_size, rings, cogs):
        self.rings = rings
        self.cogs = cogs
        ratio = rings[0] / cogs[0]
        super().__init__(wheel_size, 10)

    def shift(self, ring_idx, cog_idx):
        return self.rings[ring_idx] / self.cogs[cog_idx]


inches_per_metre = 39.37


class MountainBike(Bike):
    @classmethod
    def from_metric(cls, size_metres, ratio):
        return cls(size_metres * inches_per_metre, ratio)


class Recumbent(Bike):
    @staticmethod
    def is_fast():
        return True


tan = Tandem(26, [42, 36], [24, 20, 15, 11])
print(tan.shift(1, -1))
print(tan.gear_inches())

mtn = MountainBike.from_metric(.559, 38 / 11)
print(mtn.gear_inches())

lawnchair = Recumbent(20, 20)
print(lawnchair.is_fast())
print(lawnchair.gear_inches())
