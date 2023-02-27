import math


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

    d = b * b - 4 * a * c
    print("Discriminant is ", d)

    if d < 0:
        return "This equation have not solutions"
    if d == 0:
        root = -b / 2 * a
        return "This equation have one root: " + str(root)

    root_1 = (-b - math.sqrt(d)) / (2 * a)
    root_2 = (-b + math.sqrt(d)) / (2 * a)

    return "This equation have two solutions: root first - " + str(root_1) + " and root second - " + str(root_2)


res = quadratic_equation()
print(res)
