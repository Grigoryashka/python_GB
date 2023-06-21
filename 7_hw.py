from pprint import pprint
from math import sin


# Задача 34
"""
vowels: str = "АаЕеЁёИиОоУуЫыЭэЮюЯя"


def vowels_func(phrase):
    phrase_list = list(map(str, phrase.split()))
    k = 0    # постоянное кол-во гласных
    for i in phrase_list:
        c = 0    # переменное кол-во гласных
        if phrase_list.index(i) == 0:
            for s in i:
                if s in vowels:
                    c += 1
                    k += 1
        else:
            for s in i:
                if s in vowels:
                    c += 1
        if c != k:
            print("Пам парам")
            break
    if c == k:
        print("Парам пам-пам")


vowels_func(input())
"""


# Задача 36


def print_operation_table(operation, num_rows, num_columns):
    # def operation(num_rows, num_columns):
    a = [[0]*num_rows for n in range(num_columns)]
    for i in range(num_columns):
        for j in range(num_rows):
            a[i][j] = operation(i+1, j+1)
    return a


pprint(print_operation_table(lambda x, y: x * y, 6, 6))
