#Вариант - 5
numb=int(input("Введите число "))
if numb<0 or numb>100:
    print("Ошибка диапазона")
elif 0<=numb<=24:
    print("Мало")
elif 25<=numb<=74:
    print("Достаточно")
else:
    print("Много")
