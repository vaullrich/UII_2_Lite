# Найти количество цифр 5 в числе

res = 0
num = ''
i = 0
while not num.isdigit():
    num = input('Введите число ')

count = len(num)
while i < count:
    numTmp = int(num[i])
    if numTmp == 5:
        res += 1
    i += 1

print("Пятерок в числе {} - {}".format(num, res))