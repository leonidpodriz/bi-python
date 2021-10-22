def sum(*args):
    number = 0
    for arg in args:
        number += arg
    return number


params = (3, 4, 3)

print(sum(3, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10))

print(sum(*params))
