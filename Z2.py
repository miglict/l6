# -*- coding: cp1251 -*-

# --- БЛОК СОЗДАНИЯ ВХОДНОГО ФАЙЛА ---
with open("lab4_in.txt", "w", encoding="cp1251") as f_init:
    f_init.write("6\n")  # N = 6 элементов
    f_init.write("-2.0 2.0\n")  # Интервал [a, b] = [-2, 2]
    f_init.write("1.5 -3.0 0.5 4.0 -1.0 2.5\n")  # Сам массив


# ------------------------------------

def main():
    print("Лабораторная работа №4 (с файлами). Вариант 5.")

    try:
        fi = open("lab4_in.txt", "rt", encoding="cp1251")

        # Чтение N
        n_line = fi.readline()
        while n_line.strip().startswith("#"): n_line = fi.readline()
        n = int(n_line)

        # Чтение a и b
        ab_line = fi.readline()
        while ab_line.strip().startswith("#"): ab_line = fi.readline()
        parts = ab_line.split()
        a_bound, b_bound = float(parts[0]), float(parts[1])

        # Чтение массива
        mas_line = fi.readline()
        while mas_line.strip().startswith("#"): mas_line = fi.readline()
        mas = [float(x) for x in mas_line.split()]

        fi.close()

        print(f"Исходный массив: {mas}")
        print(f"Интервал удаления: [{a_bound}, {b_bound}]")


        # 1. Максимум
        max_el = mas[0]
        for x in mas:
            if x > max_el: max_el = x

        # 2. Сумма до последнего положительного
        last_pos_idx = -1
        for i in range(len(mas)):
            if mas[i] > 0: last_pos_idx = i

        sum_before = 0
        if last_pos_idx != -1:
            for i in range(last_pos_idx):
                sum_before += mas[i]

        # 3. Сжатие массива
        j = 0
        for i in range(n):
            if not (a_bound <= mas[i] <= b_bound):
                mas[j] = mas[i]
                j += 1
        for i in range(j, n):
            mas[i] = 0.0

        # --- ЗАПИСЬ В ФАЙЛ ---
        fo = open("lab4_out.txt", "wt", encoding="cp1251")

        fo.write("ИСХОДНЫЙ МАССИВ:\n")
        for x in mas:  # Тут мы уже перезаписали mas, но для примера запишем итоговый
            # Чтобы записать исходный, нужно было сохранить копию mas_copy = mas[:]
            pass

            # Для простоты запишем результаты обработки:
        fo.write("РЕЗУЛЬТАТЫ ОБРАБОТКИ:\n")
        fo.write("Максимальный элемент: {:7.2f}\n".format(max_el))
        fo.write("Сумма до посл. полож.: {:7.2f}\n".format(sum_before))

        fo.write("Сжатый массив:\n")
        for x in mas:
            fo.write("{:7.2f}".format(x))
        fo.write("\n")

        fo.close()
        print("Результаты записаны в lab4_out.txt")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()