from random import uniform


n = 10
array = [uniform(0, 49) for _ in range(n)]
print(f'Изначальный массив - {array}')


def sort_merge(array):
    if len(array) <= 1:
        return array[:]
    else:
        mid = len(array) // 2
        left = sort_merge(array[:mid])
        right = sort_merge(array[mid:])

        return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


print(f'Отсортированный массив - {sort_merge(array)}')
