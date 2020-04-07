def f(x):
    return 2*x


def g(x, b):
    a = 3*b
    return f(2) + a


def h(x, y, s=None):
    if s is not None:
        return f(2) + g(f(2)) + x + y
    else:
        return f(2) + g(f(2)) + x*y


class Teste:

    def __init__(self):
        pass

    def method_a(self):
        pass

    def method_b(self):
        self.method_a()
        f(2)