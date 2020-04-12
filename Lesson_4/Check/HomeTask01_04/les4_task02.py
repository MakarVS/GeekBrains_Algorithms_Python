# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».


# Решение - вариант №1 с использованием Решета Эратосфена. В основе предположение, что n-е простое число приблиительно равно n*ln(n). Для малых значений
# 2-2.5*ln(n). Чтобы оптимизировать алгортм, предполагаем, что первые 5 чисел нам известны и их не надо вычислять, тем самым снижая количество вычислений при
#больших значчениях n.


import timeit
import cProfile

from math import log
def resheto (n):
    known_siev=[2,3,5,7,11]
    if n<=5:

        return known_siev [n-1]

    else:
        k= round(1.4*n*log(n))
        siev=[i for i in range (k)]
        siev[1]=0
        for i in range (2,k):
            if siev [i]!=0:
                j=i*2
                while j<k:
                    siev [j]=0
                    j+=i


        result = [result for result in siev if result!=0]
        return result [n-1]

#Второй алгоритм поочередно проверяет делимость числа i на делители от 2 до i/2+1 Если число не делется, оно считается простым, добавляется в список.
# алгоритм проверяет количество элементов в списке, и если их меньше n, увеличивает i на 1 и повторяет проверку

def siev_loop (n):
    result=[2]
    i=3
    while len(result)<n:

        for j in result:
           #print (i,j)
           if i%j==0:
               break
           else:
               if 2*j>i:
                    result.append(i)
                    #print (result)
                    break

        i=i+1
    return result[n-1]

n=int(input("Задайте число - порядковый номер простого числа: "))
print (f"Результат методом Решета Эратосфена: {resheto (n)}")

#Результаты проверки первого алгоритма по timeit для loop=1000

#print (timeit.repeat("for x in range(150): resheto(x)", "from __main__ import resheto", number=1000))


#n=10
#[0.4339358, 0.2675059000000001, 0.45498649999999996, 0.3788134999999999, 0.26897210000000005]
#n=20
#[1.3018707, 1.1147395000000002, 0.7825757000000002, 1.2723803999999999, 0.9585950000000008]
#n=50
#[15.3248033, 22.3281571, 21.603125899999995, 15.419275900000002, 23.032114199999995]
#n=100
#[88.67338369999999, 129.1911328, 95.9796182, 89.78087650000003, 86.11860860000002]
#n=150
#[209.32799640000002, 173.43050350000001, 156.3646132, 169.38081709999994, 143.725324]

#Результаты проверки первого алгоритма по cProfie
#cProfile.run ("resheto(10000000)")
#n=10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:16(resheto)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:34(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#n=20
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:16(resheto)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:34(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=100
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les4_task2.py:16(resheto)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:24(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:34(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=1000
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.017    0.017    0.021    0.021 les4_task2.py:16(resheto)
#         1    0.002    0.002    0.002    0.002 les4_task2.py:24(<listcomp>)
#         1    0.002    0.002    0.002    0.002 les4_task2.py:34(<listcomp>)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=10000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.318    0.318 <string>:1(<module>)
#         1    0.276    0.276    0.316    0.316 les4_task2.py:16(resheto)
#         1    0.026    0.026    0.026    0.026 les4_task2.py:24(<listcomp>)
#         1    0.014    0.014    0.014    0.014 les4_task2.py:34(<listcomp>)
#         1    0.000    0.000    0.318    0.318 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=100000
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.024    0.024    3.537    3.537 <string>:1(<module>)
#         1    2.830    2.830    3.513    3.513 les4_task2.py:16(resheto)
#         1    0.527    0.527    0.527    0.527 les4_task2.py:24(<listcomp>)
#         1    0.156    0.156    0.156    0.156 les4_task2.py:34(<listcomp>)
#         1    0.000    0.000    3.537    3.537 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=1000000
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.299    0.299   41.990   41.990 <string>:1(<module>)
#         1   36.500   36.500   41.691   41.691 les4_task2.py:16(resheto)
#         1    2.931    2.931    2.931    2.931 les4_task2.py:24(<listcomp>)
#         1    2.260    2.260    2.260    2.260 les4_task2.py:34(<listcomp>)
#         1    0.000    0.000   41.990   41.990 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#         1    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=10 000 000
# MemoryError


print (f"Результат методом Цикла: {siev_loop (n)}")

#Результаты проверки второго алгоритма по timeit для loop=1000
#print (timeit.repeat("for x in range(150): siev_loop(x)", "from __main__ import siev_loop", number=1000))


#n=10
# [0.22137210000000002, 0.2544978, 0.24221700000000002, 0.20597469999999996, 0.17544369999999998]
#n=20
#[1.9501614999999999, 1.3437787, 1.4747, 1.4815038000000005, 1.951061000000001]
#n=50
#[16.4345407, 15.1320051, 20.781953499999997, 17.0939392, 18.624800499999992]
#n=100
# [103.6031033, 106.13382560000001, 119.48194680000003, 117.01115689999995, 113.21247069999998]
#n=150
# [317.3008643, 347.98760200000004, 339.2512565999999, 298.5128264000001, 388.4033555000001]

#Результаты проверки второго алгоритма по cProfie
#cProfile.run ("siev_loop(100000)")
# n=10
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:40(siev_loop)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=20
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les4_task2.py:40(siev_loop)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        70    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        19    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=50
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les4_task2.py:40(siev_loop)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       228    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        49    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=500
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.086    0.086 <string>:1(<module>)
#         1    0.080    0.080    0.086    0.086 les4_task2.py:40(siev_loop)
#         1    0.000    0.000    0.086    0.086 {built-in method builtins.exec}
#      3570    0.006    0.000    0.006    0.000 {built-in method builtins.len}
#       499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=1000
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.328    0.328 <string>:1(<module>)
#         1    0.323    0.323    0.328    0.328 les4_task2.py:40(siev_loop)
#         1    0.000    0.000    0.328    0.328 {built-in method builtins.exec}
#      7918    0.004    0.000    0.004    0.000 {built-in method builtins.len}
#       999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#n=10000
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   20.709   20.709 <string>:1(<module>)
#         1   20.648   20.648   20.708   20.708 les4_task2.py:40(siev_loop)
#         1    0.000    0.000   20.709   20.709 {built-in method builtins.exec}
#    104728    0.045    0.000    0.045    0.000 {built-in method builtins.len}
#      9999    0.016    0.000    0.016    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




