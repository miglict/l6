# -*- coding: cp1251 -*-
from math import sin, cos, pi

# --- БЛОК ДЛЯ СОЗДАНИЯ ВХОДНОГО ФАЙЛА
with open("lab1_in.txt", "w", encoding="cp1251") as f_init:
    f_init.write("# Входные данные для Лаб 1\n")
    f_init.write("# alpha\n")
    f_init.write("1.5\n")  # альфа = 1.5 радиан


# -----------------------------------------------------------------------------

def main():
    print("Лабораторная работа №1 (с файлами). Вариант 5.")

    try:
        # 1. Чтение из файла
        fi = open("lab1_in.txt", "rt", encoding="cp1251")

        # Пропускаем строки-комментарии
        line = fi.readline()
        while line.startswith("#"):
            line = fi.readline()

        # Теперь в line должно быть число
        alpha = float(line.strip())
        fi.close()

        print(f"Прочитано alpha = {alpha}")

        # 2. Вычисления
        z1 = 1 - 0.25 * (sin(2 * alpha)) ** 2 + cos(2 * alpha)
        z2 = (cos(alpha)) ** 2 + (cos(alpha)) ** 4

        # 3. Запись в файл
        fo = open("lab1_out.txt", "wt", encoding="cp1251")
        fo.write("Результаты вычислений:\n")
        # Используем форматирование как в методичке
        fo.write("Z1 = {:7.4f}\n".format(z1))
        fo.write("Z2 = {:7.4f}\n".format(z2))
        fo.close()

        print("Результаты успешно записаны в lab1_out.txt")

    except FileNotFoundError:
        print("Ошибка: Файл lab1_in.txt не найден!")
    except ValueError:
        print("Ошибка: Неверный формат данных в файле.")


if __name__ == "__main__":
    main()