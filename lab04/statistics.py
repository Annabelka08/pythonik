n=int(input("Введите количество чисел "))
summ=0
polozh=0
mx=-99*10**100

for _ in range(n):
    i=int(input("Введите число "))
    summ+=i
    if i>=0:
        polozh+=1
    if i>mx:
        mx=i
print(f"Сумма равна {summ}, число положительных значений - {polozh}, максимум - {mx}")