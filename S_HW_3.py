# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [3,5,8,9,10,12,13]
print(sum(list[1::2]))

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [10, 14, 8, 2, 20]
result_list = []
for i in range((len(list)+1)//2):
    result_list.append(list[i]*list[len(list)-1-i])
print(result_list)
# 
list = [10, 14, 2, 20]
result_list = []
for i in range((len(list)+1)//2):
    result_list.append(list[i]*list[len(list)-1-i])
print(result_list)

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

list = [2, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max-min)

# Напишите программу, 
# которая будет преобразовывать десятичное число в двоичное.

n = int(input('Введите десятичное число : '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)
