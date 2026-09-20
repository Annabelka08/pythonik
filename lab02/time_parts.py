total_seconds=int(input("Введите количество секунд "))
hours=total_seconds//3600
minuts=(total_seconds-(hours*3600))//60
seconds=total_seconds-(hours*3600)-(minuts*60)
print(f' {hours} ч. {minuts} мин. {seconds} с.')