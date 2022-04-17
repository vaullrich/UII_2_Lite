# Вывести цифры числа на каждой новой строке.
num = ''
i = 0
while not num.isdigit():
    num = input('Введите число ')
count = len(num)
while i < count:
    print(num[i])
    i += 1
