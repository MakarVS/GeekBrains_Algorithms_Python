from random import uniform

# Сортировка слиянием состоит из двух функций - разделения на части и склейки результата

def merge(A, B):
    C = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < len(A):
        C.extend(A[i:])
    if j < len(B):
        C.extend(B[j:])
    return C


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        LL = merge_sort(L[:middle])
        LR = merge_sort(L[middle:])
        return merge(LL, LR)


n = int(input('Размер списка: '))
A = [uniform(0, 49) for i in range(n)]
print('Было: ', A)
C = merge_sort(A)
print('Стало: ', C)

#Размер списка: 6
#Было:  [34.00349815890533, 29.70226993498734, 21.56282504727895, 8.840614867962936, 10.043163359088341, 37.17218679376623]
#Стало:  [8.840614867962936, 10.043163359088341, 21.56282504727895, 29.70226993498734, 34.00349815890533, 37.17218679376623]