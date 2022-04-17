# Вывести на экран циклом пять строк из нулей длиной 4, причем каждая строка должна быть пронумерована.
i = 0
count = 5
charsCount = 4
while i < count:
    j = 0
    text = ''
    while j < charsCount:
        text += '0'
        j += 1
    print(i, text)
    i += 1