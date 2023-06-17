import codecs
from pprint import pprint


def delete(file, pers):
    return file.pop(pers)


def change(file, pers):
    data = file[pers].split()
    n = int(input())
    if n == 1:
        print("Введите новое имя:")
        new_name = input()
        data[1] = new_name
        file[pers] = " ".join(data) + "\r\n"
        print(file[pers].split())
    elif n == 2:
        print("Введите новую фамилию:")
        new_sname = input()
        data[0] = new_sname
        file[pers] = " ".join(data) + "\r\n"
        print(file[pers].split())
    elif n == 3:
        print("Введите новое отчество:")
        new_fname = input()
        data[2] = new_fname
        file[pers] = " ".join(data) + "\r\n"
        print(file[pers].split())
    elif n == 4:
        print("Введите новый телефон:")
        new_phone = input()
        data[3] = new_phone
        file[pers] = " ".join(data) + "\r\n"
        print(file[pers].split())


f = codecs.open("phone_numbers.txt", "r", "utf-8")
# pprint(f.readlines())
a = f.readlines()
print("Введите ключевое слово для поиска:")
value = input()
values = []
for i in a:
    if value in i:
        values.append(f"{a.index(i)} {i}")
pprint(values)
print("Выберите нужного человека из отфильтрованного списка (введите его номер):")
num = int(input())
print(a[num])
print("Выберите опцию: удалить(1) или изменить(2)")
option = int(input())
if option == 1:
    delete(a, num)
elif option == 2:
    print("Что вы хотите изменить? Имя(1), фамилию(2), отчество(3), телефон(4)")
    change(a, num)
pprint(a)
with codecs.open("phone_numbers.txt", "w", "utf-8") as f:
    f.writelines(a)

#f.close()
