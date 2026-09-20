nazv = input("Введите название заказа ")
imya =input("Введите имя заказчика ")
name1=input("Введите название первой позиции ")
name2=input("Введите название второй позиции ")
col1=int(input("Введите количество для первой позиции "))
col2=int(input("Введите количество для второй позиции "))
price1 =int(input("Введите цену для первой позиции "))
price2 =int(input("Введите цену для второй позиции "))
dostavka =int(input("Введите стоимость доставки "))
vnesli=int(input("Введите внесенную сумму"))

cost1=col1*price1
cost2=col2*price2
obshay=cost1+cost2
sm=obshay+dostavka
col=col1+col2
sdacha=vnesli-sm

print(f"-----{nazv}-----")
print(f'Имя заказчика {imya}')
print(f'Название-{name1} | Количнство-{col1} | Цена-{price1} | Стоимость-{cost1}')
print(f'Название-{name2} | Количнство-{col2} | Цена-{price2} | Стоимость-{cost2}')
print(f"Стоимость товаров без доставки - {obshay:2f} руб.")
print(f'Общая сумма с доставкой - {sm:2f} руб.')
print(f"Общее количество единиц-{col}")
print(f"Сдача {sdacha:2f}")





