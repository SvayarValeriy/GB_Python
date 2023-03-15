'''
Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
'''

#Два варианта решения

n = list(map(int, list(input('Enter ticket number: '))))
print('Yes' if sum(n[:3]) == sum(n[3:]) else 'No')



n = int(input('Emter ticket number: '))
left = sum(map(int, str(n // 1000)))
right = sum(map(int, str(n % 1000)))
if left == right:
    print('Yes')
else:
    print('No')