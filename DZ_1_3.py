# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
flo = []
max = 0
min = 0

for i in range(len(my_list)):
    flo.append(my_list[i]%1)
print("Without int:", flo)

for i in range(len (flo)):
    flo=[round(v,3) for v in flo]
print("Raund number:", flo)

for i in range(len(flo)):
    if flo[i] > flo[0]:
        max = flo[i]
print("Max number:", max)

for i in range(len(flo)):
    if flo[i] < flo[0] and flo[i] != 0:
        min = flo[i]
print("Min number:", min)
print("Answer:", max - min)








