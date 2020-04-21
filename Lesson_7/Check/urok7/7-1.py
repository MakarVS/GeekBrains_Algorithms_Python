from random import randint


# функция сортирует массив пузырьком, оптимизация - если обмено не было, то готово
# ничего не возвращает, т.к. сортирует переданный (по ссылке) массив (список)
def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        flag = False  # флаг был ли обмен
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                flag = True
        if not flag:  # если обменов не было
            break  # все отсотрировано


n = int(input('Размер списка: '))
A = [randint(-100, 99) for i in range(n)]
print('Было: ', A)
bubble_sort(A)
print('Стало: ', A)
