s=input("Введите строку ")
s1=s[1:-1]
s2=""
s1=s1.split(" ")
for elem in s1:
    if elem!='':
        s2+=elem
        s2+=' '

print(f"Исходная длина - {len(s)}")
print(f"Новая длина - {len(s2)}")
print(f"Нормализированный текст - {s2}")
print(f"Количество слов - {len(s2.split(' '))-1}")





