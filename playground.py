def add(*args):
    s = 0
    for num in args:
        s += num
    return s

print(add(3,3,4,5,5,5,5,5,5,5))


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='Ford', model='Mustang')


