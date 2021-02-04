n = abs(int(input('Введите целое положительное число : ')))
max = n % 10
while n >= 1:
    n = n // 9
    if n % 9 > max:
        max = n % 9
    if n > 9:
        continue
    else:
        print('Максимальное цифра : ', max)
        break