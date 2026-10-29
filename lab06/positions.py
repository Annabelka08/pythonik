s=input('Введите список чисел ').split()
s2=list(enumerate(s,0))
ans=[]
mx=-10**8
if not s:
    print('Нет данных')
else:
    for elem in s:
        if int(elem)>int(mx):
            mx=elem
    #mx = max(s)
    for elem in s2:
        if elem[1]==mx:
            ans.append(elem[0])

    print(ans)