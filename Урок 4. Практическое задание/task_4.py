"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 3, 3, 3, 1, 3, 4, 5, 1, 3, 5, 6, 7, 2, 2, 2, 2, 54, 65, 4, 3, 5, 6, 6, 6, 6, 5, 4, 4, 32, 23, 45, 4, 32,
         432, 4,
         324, 234, 234, 32, 546, 3, 234, 4, 32, 4, 234, 32, 432, 4, 3, 3, 2, 5, 5, 5, 2, 21, 34, 4, 32, 4, 234, 234, 23,
         4231, 4, 1234, 32, 4]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    return f'Чаще всешо встречается число {max(set(array), key=lambda k: array.count(k))}, оно появилось в массиве ' \
           f'{array.count(max(set(array), key=lambda k: array.count(k)))} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(f'Время выполнения функции revers  {timeit("func_1()", globals=globals(), number=1000)}')
print(f'Время выполнения функции revers  {timeit("func_2()", globals=globals(), number=1000)}')
print(f'Время выполнения функции revers  {timeit("func_3()", globals=globals(), number=1000)}')

''' Функция 3 быстрее остальных функций, тк там используется итератор и используется множесвто, чтобы не перебирать одни
и теже значения. Не смотря на 2 вычисления значения при выводе данных , функция 3 работает быстрее в ~1,5 раза'''
