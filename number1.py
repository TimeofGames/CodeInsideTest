from random import randint


def quick_sort_median(array):
    if len(array) <= 1:
        return array

    support_element = (array[0] + array[-1] + array[len(array) // 2]) // 3

    left = list(filter(lambda x: x < support_element, array))
    center = [i for i in array if i == support_element]
    right = list(filter(lambda x: x > support_element, array))

    return quick_sort_median(left) + center + quick_sort_median(right)


lenght = int(input("Введите длинну массива "))
minimum = int(input("Введите минимум "))
maximum = int(input("Введите максимум "))
array = []

for _ in range(lenght):
    array.append(randint(minimum, maximum))
print(array)
array = quick_sort_median(array)
print(array)
