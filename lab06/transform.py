s=input('Введите список чисел ').split()
s1=[]
for elem in s:
    if int(elem)<0:
        s1.append(elem[1:])
    else:
        s1.append(elem)
print(f'Исходный список {s}')
print(f'Новый список {s1}')