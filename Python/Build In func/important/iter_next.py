# Makes anything iterable into an iterator object, it will always iterate into the next item, if it hits the end will
# throw an error, iter ( iterable) or iter ( function[ iterable], stoper), when stops will throw an error
import random
# a = iter([1,2,3,4,5,6,7,8,9,10])
# b = iter('hey')
# print(a)
#
# print(next(a))
# print(next(b))
#
# print('dawdaw')
#
# for i in range(0,10):
#
#     dawda= i+i
#
# print(next(a))
# print(next(b))


# ------------------------ #

def randoma():
    return random.randrange(1,100)

ite = iter(randoma,5)

while True:
    try:
        print(next(ite))

    except:
        print('d')
        break