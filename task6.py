'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''

inputValue = input("Введите число: ")
firstSummValue = 0
secondSummValue = 0
count = 0
if len(inputValue) < 6 or len(inputValue) > 6 :
    print("Введите 6-значное число!")
for i in inputValue :
    if count <= len(inputValue) / 2 - 1 :
        firstSummValue += int(inputValue[count])
        count += 1
    else :
        secondSummValue += int(inputValue[count])
        count += 1
if firstSummValue == secondSummValue :
    print("Yes")
else :
    print("No")
    