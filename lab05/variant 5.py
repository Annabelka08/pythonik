s=input("Введите строку ")
s1=s.split(' ')
col=0
s2=[]
for elem in s1:
    elem = elem.strip(".,!?;:")
    elem=elem.lower()
    if elem[-1]=='а':
        col+=1
        s2.append(elem)
if col==0:
    print('Нет совпадений')
    print('Общее количество слов - 0')
else:
    print(*s2,sep='\n')
    print(f'Общее количество слов - {col}')

