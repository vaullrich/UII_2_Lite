# Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
numCount = 10
i = 0
resCount = 0
while i < numCount:
    text = "Введите {}-е число: ".format(i+1)
    num = input(text)
    if not num.isdigit():
        continue
    if int(num) == 5:
        resCount += 1
    i += 1

print("Количество введенных пятерок: {}".format(resCount))