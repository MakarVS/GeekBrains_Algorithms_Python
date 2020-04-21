from random import randint, choice

# Поиск медианы в списке

m = 5
n = 2 * m + 1
A = [randint(0, 100) for i in range(n)]
print('Исходный массив: ', A)

# Можно было бы и так:
# A.sort()
# median = A[n // 2]
# print(A)
# print(median)
# [19, 5, 22, 83, 48, 48, 79, 15, 71, 0, 6]
# [0, 5, 6, 15, 19, 22, 48, 48, 71, 79, 83]

# Другой способ (без сортировки):
def quick_median(L):
    return median(L, len(L) // 2)

def median(L, k):
    if len(L) == 1:
        return L[0]

    pivot = choice(L)
    lows = []
    pivots = []
    highs = []
    for x in L:
        if x < pivot:
            lows.append(x)
        elif x == pivot:
            pivots.append(x)
        else:
            highs.append(x)

    if k < len(lows):  # элемент слева
        return median(lows, k)
    elif k < len(lows) + len(pivots):  # попали
        return pivots[0]
    else:  # элемент справа
        return median(highs, k - len(lows) - len(pivots))


print('Медиана = ', quick_median(A))
# для проверки
A.sort()
print('Отсортированный массив: ', A)
