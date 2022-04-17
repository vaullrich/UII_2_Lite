# Найти сумму цифр числа.

sum = 0
num = ''
i = 0
while not num.isdigit():
    num = input('Введите число ')

count = len(num)
while i < count:
    sum += int(num[i])
    i += 1

print("Сумма цифр числа {} - {}".format(num, sum))