# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

a = list(map(int, input().split()))
print(a)
a_length = len(a)
sum = 0
count = 1
while count < a_length:
    sum = sum + a[count]
    count = count + 2
print(sum)    
 
    
    