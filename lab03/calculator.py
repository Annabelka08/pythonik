a=float(input("Введите первое число "))
b=float(input("Введите второе число "))
oper=input("Введите операцию ")
if oper=="+":
    print(f'{a+b:.2f}')
elif oper=="-":
    print(f'{a-b:.2f}')
elif oper=="*":
    print(f'{a*b:.2f}')
elif oper=="/":
    if b==0:
        print('Деление на ноль запрещено')
    else:
        print(f'{a/b:.2f}')
else:
    print('Неизвестная операция')
