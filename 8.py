# Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
# Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".

haveFive = False
num = ''
i = 0
while not num.isdigit():
    num = input('Введите число ')

count = len(num)
while i < count:
    if int(num[i]) == 5:
        print('Цифра 5 есть в числе', num)
        haveFive = True
        break
    i += 1

if not haveFive:
    print("Цифры 5 нет в числе", num)