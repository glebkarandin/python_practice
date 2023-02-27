print("Hello world")


def quadratic_equation():
    a = input("Input a: ")
    b = input("Input b: ")
    c = input("Input c: ")

    if a.isnumeric():
        a = int(a)
    else:
        a = 0

    if b.isnumeric():
        b = int(b)
    else:
        b = 0

    if c.isnumeric():
        c = int(c)
    else:
        c = 0

    d = b - 4 * a * c
    return d


res = quadratic_equation()
print(res)
