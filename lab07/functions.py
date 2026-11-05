def sum_digits(number):
    s=0
    n=abs(number)
    for elem in str(n):
        s+=int(elem)
    return s

#print(sum_digits(0))


def average(numbers):
    if not numbers:
        return None
    else:
        col=0
        s=0
        for elem in numbers:
            s+=elem
            col+=1
        return s/col
#print(average([]))

def normalize_text(text):
    t=text.lower()
    t2=''
    t=t.split(' ')
    for elem in t:
        if elem != '':
            t2+=elem
            t2+=' '
    return t2[:-1]

#print(normalize_text(' ВАП    укаКАЕПР УВАП  '))

#Вариант 5
def select_numbers(numbers, threshold):
    numb=[]
    for elem in numbers:
        if int(elem) <= int(threshold):
            numb.append(elem)
    return numb
#print(select_numbers([-5, 0, 1, 2, 1, 2, 5], 2))





