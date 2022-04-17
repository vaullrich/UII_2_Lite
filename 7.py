# Найти произведение цифр числа.

res = 0
num = ''
i = 0
while not num.isdigit():
    num = input('Введите число ')

count = len(num)
while i < count:
    if i == 0:
        res = int(num[i])
    else:
        res *= int(num[i])
    i += 1

print("Произведение цифр числа {} - {}".format(num, res))