s=input('Введите целые числа одной строкой ').split()
col=0
suma=0
for elem in s:
    col+=1
    suma+=int(elem)
if col==0:
    print('Нет данных')
else:
    print(f'Количиство чисел - {col}')
    print(f'Сумма чисел - {suma}')
    print(f'Минимальное значение - {min(s)}')
    print(f'Максимальное значение - {max(s)}')
    print(f'Среднее значение - {suma/len(s):.2f}')

