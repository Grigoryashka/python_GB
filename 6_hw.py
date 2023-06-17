# Задача 30
print("Введите первый элемент, разность арифметической прогрессии и количество элементов(каждое значение с новой "
      "строки):")
a1 = int(input())
d = int(input())
n = int(input())
a = [a1]
for i in range(2, n+1):
    a.append(a[0] + (i - 1) * d)
print(f"Полученные числа прогрессии: {a}")


# Продолжение, 32 задача
indexes = []
print("Теперь введите диапазон через пробел:")
diap = list(map(int, input().split()))
for i in range(n):
    if diap[0] <= a[i] <= diap[1]:
        indexes.append(i)
print(f"Индексы элементов массива, которые попадают в заданный диапазон: {indexes}")


