'''
У вас есть массив чисел, составьте из них максимальное число. 
'''

import random
m = [random.randint(1, 300) for i in range(4)]
print(m) #Создаем рандомный массив из 4 чисел, в указанном диапазоне
print(''.join((sorted([str(x) for x in m], reverse=True))))