# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
# Вам поручили создать генератор ландшафта. Напишите программу, которая
# получает на вход число N и выводит на экран числа в виде ямы:
N = int(input("Введите число N: "))
for i in range(1, N + 1):
    left_part = ''.join(str(x) for x in range(N, N - i, -1))
    right_part = ''.join(str(x) for x in range(N-i+1, N+1))
    spaces = '.' * (2 * (N - i))
    print(left_part + spaces + right_part)

