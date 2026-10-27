s=input("Введите строку ")
s1=s.replace(" ","")
if s1=="":
    print("Нет текста")
else:
    s1=s1.lower()
    if s1==s1[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")