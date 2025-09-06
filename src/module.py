def f(a):
    if isinstance(a, int):
        return a ** 2
    raise TypeError("Unsupported type")
