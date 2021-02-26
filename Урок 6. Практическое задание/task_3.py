"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

"""

Для профилирования рекурсии необходимо создовать дополнительную функцию, внутри которой вызывать рекурсию
и профилировать именно эту отдельную функцию. В противном случае профилировщик будет вызываться столько раз,
сколько запускается рекурсия.

"""

from memory_profiler import profile


def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


@profile()
def wrapper(n):
    return fibonacci(n)


n = int(input("Введите число членов последовательности:"))
print("Последовательность Фибоначчи:")
for i in range(n):
    print(fibonacci(i))

wrapper(n)


