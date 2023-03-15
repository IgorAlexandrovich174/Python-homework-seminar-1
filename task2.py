'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''

value = input('Введите число: ')
result = 0
for i in value :

    if len(value) < 3 :
        print("Ввели некорректное число!")
        break
    else :
        result += int(i)
print(result)

