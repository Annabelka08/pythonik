#Вариант 5
s=input('Введите целые числа одной строкой ').split()
s2=[]
col=0
sm=0
for elem in s:
    if int(elem)>0:
        s2.append(int(elem))
        col+=1
        sm+=int(elem)
print(s2)
print(col)
print(sm)
print(sorted(s2))
