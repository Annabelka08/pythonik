from functions import sum_digits
number=int(input('Введите целое число '))
result1 = sum_digits(number)
print('Результат:', result1)

from functions import average
raw2 = input('Введите список чисел: ')
numbers=[int(x) for x in raw2.split()]
result2=average(numbers)
print('Результат:', result2)

from functions import normalize_text
text=input('Введите текст: ')
result3=normalize_text(text)
print('Результат:', result3)

from functions import select_numbers
raw = input("Введите список целых чисел через пробел: ")
numbers = [int(x) for x in raw.split()]
threshold = int(input("Введите порог (неотрицательное целое число): "))
result4 = select_numbers(numbers, threshold)
print("Результат:", result4)