# Найти максимальную цифру в числе

res = 0
num = ''
i = 0
while not num.isdigit():
    num = input('Введите число ')

count = len(num)
while i < count:
    numTmp = int(num[i])
    if res < numTmp:
        res = numTmp

    i += 1

print("Максимальная цифра в числе {} - {}".format(num, res))