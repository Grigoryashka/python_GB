# Задача 28


"""def tree_add(level, p):
    if level == 0:
        a, b = p
        if b == 0:
            return a, 0
        if b > 0:
            return a + 1, b - 1
        if b < 0:
            return a - 1, b + 1
    return tree_add(level - 1, tree_add(level - 1, p))


def linear_add(level, p):
    a, b = tree_add(level, p)
    if b == 0:
        return a
    return linear_add(level + 1, (a, b))


def add(a, b):
    return linear_add(0, (a, b))


print("Введите 2 числа:")
numbers = list(map(int, input().split()))
numbers.sort()
print(f"Сумма введенных вами чисел: {add(numbers[1], numbers[0])}")"""


# Задача 26
def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        return pow(a, b-1)*a


print("Введите число и его степень через пробел:")
pows = list(map(int, input().split()))
print(f"Число {pows[0]} в степени {pows[1]}: {pow(pows[0], pows[1])}")
