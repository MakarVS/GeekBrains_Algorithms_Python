l1 = int(input('введите длину 1 отрезка '))
l2 = int(input('введите длину 2 отрезка '))
l3 = int(input('введите длину 3 отрезка '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 != l2 != l3:
        print('разносторонний')
    elif l1 == l2 == l3:
        print('равносторонний')
    else:
        print('равнобедренный')
else:
    print('такого треугольника не существует')