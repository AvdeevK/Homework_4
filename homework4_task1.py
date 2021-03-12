#  1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
#     первых трех уроков.


# Задача 4 из д/з к уроку 2. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


import timeit
import cProfile


# 1. Поиск суммы ряда через рекурсию

def summator_rec(n):
    if n == 1:
        s = 1
        return s
    else:
        s = (-0.5) ** (n - 1)
        return s + summator_rec(n - 1)


print(timeit.timeit('summator_rec(10)', number=1000, globals=globals()))  # 0.0021717000000000004
print(timeit.timeit('summator_rec(100)', number=1000, globals=globals()))  # 0.022792999999999997
print(timeit.timeit('summator_rec(990)', number=1000, globals=globals()))  # 0.3073644

cProfile.run('summator_rec(990)')


#       993 function calls (4 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#  990/1    0.001    0.000    0.001    0.001 homework4_task1.py:10(summator_rec)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2. Поиск суммы ряда с помощью цикла

def summator_cycle(n):
    s = 1
    for i in range(1, n):
        s += (-0.5) ** (i)
    return s


print(timeit.timeit('summator_cycle(10)', number=1000, globals=globals()))  # 0.0016530999999999994
print(timeit.timeit('summator_cycle(100)', number=1000, globals=globals()))  # 0.0162097
print(timeit.timeit('summator_cycle(1000)', number=1000, globals=globals()))  # 0.167439
print(timeit.timeit('summator_cycle(10000)', number=1000, globals=globals()))  # 2.1293168
print(timeit.timeit('summator_cycle(100000)', number=1000, globals=globals()))  # 21.8542634
print(timeit.timeit('summator_cycle(1000000)', number=1000, globals=globals()))  # 219.4339209

cProfile.run('summator_cycle(10000)')

#       4 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1    0.002    0.002    0.002    0.002 homework4_task1.py:36(summator_cycle)
#      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('summator_cycle(100000)')

#       4 function calls in 0.022 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.022    0.022 <string>:1(<module>)
#      1    0.022    0.022    0.022    0.022 homework4_task1.py:36(summator_cycle)
#      1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('summator_cycle(1000000)')


#       4 function calls in 0.220 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.220    0.220 <string>:1(<module>)
#      1    0.220    0.220    0.220    0.022 homework4_task1.py:36(summator_cycle)
#      1    0.000    0.000    0.220    0.220 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 3. Поиск с помощью генератора множества

def summator_arr(n):
    s = 0
    arr = [(-0.5) ** (i) for i in range(n)]
    for i, item in enumerate(arr):
        s += item
    return s


print(timeit.timeit('summator_arr(10)', number=1000, globals=globals()))  # 0.0022452999999999987
print(timeit.timeit('summator_arr(100)', number=1000, globals=globals()))  # 0.0193005
print(timeit.timeit('summator_arr(1000)', number=1000, globals=globals()))  # 0.2043289
print(timeit.timeit('summator_arr(10000)', number=1000, globals=globals()))  # 2.5297746
print(timeit.timeit('summator_arr(100000)', number=1000, globals=globals()))  # 27.171131300000003
print(timeit.timeit('summator_arr(1000000)', number=1000, globals=globals()))  # 277.8799732

cProfile.run('summator_arr(10000)')

#       5 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.001    0.001    0.003    0.003 homework4_task1.py:62(summator_arr)
#      1    0.002    0.002    0.002    0.002 homework4_task1.py:64(<listcomp>)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('summator_arr(100000)')

#       5 function calls in 0.027 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.027    0.027 <string>:1(<module>)
#      1    0.006    0.006    0.026    0.026 homework4_task1.py:75(summator_arr)
#      1    0.021    0.021    0.021    0.021 homework4_task1.py:77(<listcomp>)
#      1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('summator_arr(1000000)')


#       5 function calls in 0.282 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.006    0.006    0.281    0.281 <string>:1(<module>)
#      1    0.058    0.058    0.275    0.275 homework4_task1.py:76(summator_arr)
#      1    0.217    0.217    0.217    0.217 homework4_task1.py:78(<listcomp>)
#      1    0.000    0.000    0.282    0.282 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 4. Поиск с помощью генератора множества и встроенной функции

def summator_sumarr(n):
    s = 0
    arr = [(-0.5) ** (i) for i in range(n)]
    s = sum(arr)
    return s


print(timeit.timeit('summator_sumarr(10)', number=1000, globals=globals()))  # 0.0018793999999999998
print(timeit.timeit('summator_sumarr(100)', number=1000, globals=globals()))  # 0.0155334
print(timeit.timeit('summator_sumarr(1000)', number=1000, globals=globals()))  # 0.15586850000000002
print(timeit.timeit('summator_sumarr(10000)', number=1000, globals=globals()))  # 1.9966645
print(timeit.timeit('summator_sumarr(100000)', number=1000, globals=globals()))  # 21.4919902
print(timeit.timeit('summator_sumarr(1000000)', number=1000, globals=globals()))  # 225.1487965

cProfile.run('summator_sumarr(10000)')

#       6 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1    0.000    0.000    0.002    0.002 homework4_task1.py:90(summator_sumarr)
#      1    0.002    0.002    0.002    0.002 homework4_task1.py:92(<listcomp>)
#      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('summator_sumarr(100000)')

#          6 function calls in 0.023 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.023    0.023 <string>:1(<module>)
#         1    0.000    0.000    0.022    0.022 homework4_task1.py:118(summator_sumarr)
#         1    0.022    0.022    0.022    0.022 homework4_task1.py:120(<listcomp>)
#         1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#

cProfile.run('summator_sumarr(1000000)')

#       6 function calls in 0.228 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.006    0.006    0.228    0.228 <string>:1(<module>)
#      1    0.000    0.000    0.221    0.221 homework4_task1.py:120(summator_sumarr)
#      1    0.217    0.217    0.217    0.217 homework4_task1.py:122(<listcomp>)
#      1    0.000    0.000    0.228    0.228 {built-in method builtins.exec}
#      1    0.005    0.005    0.005    0.005 {built-in method builtins.sum}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#                                                       Вывод:
#
# Для рассмотренных выше алгоритмов был проведен ряд экспериментов, согласно которым было установлено время исполнения
# данных алгоритмов для разного количества итераций.
#
# Алгоритм 1, содержащий в себе рекурсивный вызов показал худшее время исполнения для количества итераций до 1000,
# дальнейшее исполнение алгоритма невозможно в силу достижения глубины рекурсии.
#
# Алгоритм 2, содержащий в себе цикл, для количества итераций < 100_000 имеет хорошее время для каждого из замеров,
# уступая в частных случаях только алгоритму 4, однако для количества итерации > 1_000_000 он превосходит все остальные
# алгоритмы. Общее время исполнения программы является лучшим для всех попыток.
#
# Алгоритм 3, содержащий в себе генератор, показывает худшее время для всех попыток. Общее время исполнения программы
# замедляется ввиду наличия и генератора, и вложенного цикла.
#
# Алгоритм 4, в котором цикл заменен на встроенную функцию, показывает лучшее время в попытках с количеством итераций
# < 100_000, однако с ростом количества элементов ряда, исполнение алгоритма замедляется в силу того, что к общему времени
# добавляется время на исполнение встроенной функции.
#
# Проведя данное сравнение, считаю Алгоритм 2 наиболее оптимальным
