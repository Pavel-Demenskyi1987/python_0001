# Задание 1. Рамка
# Напишите программу, которая рисует прямоугольную рамку с помощью
# символьной графики. Для вертикальных линий используйте символ
# вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
# высоту рамки определяет пользователь.


shtrich_num = int(input("Введите высоту прямоугольника: "))
defis_num = int(input("Введите ширину прямоугольника: "))

for i in range(shtrich_num):
    for j in range(defis_num):
        if j == 0 or j == defis_num - 1:
            print("|", end="")
        elif i == 0 or i == defis_num - 1:
            print("-", end="")
        else:
            print(" ", end="")
    print()
