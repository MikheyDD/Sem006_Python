# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

def numbers(x):
    lst_1 = []
    for _ in range(x):
        lst_1.append(int(input('Введите элемент массива: ')))
    return lst_1


def count_pair(list_1: list):
    sum_count = 0
    for i in set(list_1):
        sum_count += list_1.count(i) // 2
    return sum_count

n = int(input('Введите количество элементов первого массива: '))
lst_n = numbers(n)
print(count_pair(lst_n))

# def count_pairs(inp_lst: list):
#     return sum([inp_lst.count(i) // 2 for i in set(inp_lst)])




        
