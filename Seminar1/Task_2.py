# Задача 2: Найдите сумму цифр трехзначного числа.
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

#Без проверок, с использованием встроенных функций

print('Enter a three-digit number please')
print('Sum of digits =', sum(map(int,input())))



# Этот вариант без проверки на плавающую точку,
# но работает на любое количество знаков

num = input()
a = 0
for i in num:
    a += int(i)

print(a)


#Ну и наконец искомое решение с проверкой на разрядность
# и тип float

while True:
    num = input('Введите трехзначное число: ')
    try:
        num = int(num)
    except ValueError:
        print('Ошибка ввода!')

    else:
        if  num < 100 or num > 999:
            print('Ошибка ввода!')
        else:
            a = num // 100
            b = num // 10 % 10  
            c = num % 10
            print( a + b + c)
            break


