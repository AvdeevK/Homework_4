# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
#    на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile


def finder(n):
    num = 0  # Задаем переменной num, хранящей целые положительные числа (1,2,3...), значение 0
    pos_nat = 0  # Задаем позицию натурального числа
    temp_num = num  # Хранит текущее натуральное
    flag = 0  # Флаг выхода из цикла

    while flag != 1:  # Цикл, прерывающийся по флагу
        num += 1  # При каждом проходе берем новое целое число
        div_counter = 0  # Обнуляем счётчик его делителей

        for i in range(1, num + 1):  # Перебираем делители
            if num % i == 0:  # Если число является делителем текущего числа
                div_counter += 1  # Увеличиваем счётчик

            if div_counter > 2:  # Если делителей уже больше, чем два
                break  # Выходим из for, чтобы не перебирать лишнее

        if div_counter <= 2:  # Делаем проверку, если натуральное (не больше двух делителей)
            temp_num = num  # Значение числа запоминаем
            pos_nat += 1  # Запоминаем его позицию
        if pos_nat == n:  # Если запомненная позиция совпадает с нужной
            flag = 1  # Устанавливаем флаг для выхода из цикла

    return temp_num


# print(timeit.timeit('finder(10)', number=1000, globals=globals()))  # 0.0397873
# print(timeit.timeit('finder(100)', number=1000, globals=globals()))  # 3.3159011
# print(timeit.timeit('finder(1000)', number=1000, globals=globals()))  # 299.7113115
#
# cProfile.run('finder(1000)')

#       4 function calls in 0.728 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.728    0.728 <string>:1(<module>)
#      1    0.728    0.728    0.728    0.728 homework4_task2.py:8(finder)
#      1    0.000    0.000    0.728    0.728 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def eratosphene(n):
    arr = [_ for _ in range(10 * n)]
    for i, item in enumerate(arr):
        if item > 1:
            for j in range(item + item, len(arr), item):
                arr[j] = 0
    arr_temp = [num for num in arr if num != 0]
    return arr_temp[n]


print(timeit.timeit('eratosphene(10)', number=1000, globals=globals()))  # 0.053981400000000006
print(timeit.timeit('eratosphene(100)', number=1000, globals=globals()))  # 0.4885111
print(timeit.timeit('eratosphene(1000)', number=1000, globals=globals()))  # 4.9133756


cProfile.run('eratosphene(1000)')

#       1235 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.002    0.002    0.003    0.003 homework4_task2.py:51(eratosphene)
#      1    0.000    0.000    0.000    0.000 homework4_task2.py:52(<listcomp>)
#      1    0.000    0.000    0.000    0.000 homework4_task2.py:57(<listcomp>)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#   1229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:
# Программа, написанная через решето Эратосфена исполняется в сотни раз быстрее, нежели самостоятельная реализация