import numpy as np

# --- БЛОК СОЗДАНИЯ ВХОДНОЙ МАТРИЦЫ ---
# Создадим файл с матрицей 3x3
test_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
np.savetxt("lab5_in.txt", test_matrix, fmt='%d')


# -------------------------------------

def SumPositiveCols(Matr):
    n = Matr.shape[0]
    total_sum = 0
    for j in range(n):
        has_neg = False
        for i in range(n):
            if Matr[i][j] < 0:
                has_neg = True
                break
        if not has_neg:
            col_sum = sum(Matr[i][j] for i in range(n))
            total_sum += col_sum
    return total_sum


def MinAntiDiagSum(Matr):
    n = Matr.shape[0]
    min_val = float('inf')
    for k in range(-(n - 1), n):
        diag_sum = 0
        count = 0
        for i in range(n):
            j = n - 1 - i + k
            if 0 <= j < n:
                diag_sum += abs(Matr[i][j])
                count += 1
        if count > 0 and diag_sum < min_val:
            min_val = diag_sum
    return min_val


def main():
    print("Лабораторная работа №5 (с файлами). Вариант 5.")

    try:
        # Чтение матрицы из файла (как в методичке стр. 90)
        MyMatr = np.loadtxt("lab5_in.txt", dtype=int)
        print("Матрица из файла:")
        print(MyMatr)

        # Вычисления
        s1 = SumPositiveCols(MyMatr)
        s2 = MinAntiDiagSum(MyMatr)

        # Запись результатов в текстовый файл
        with open("lab5_out.txt", "wt", encoding="cp1251") as fo:
            fo.write("РЕЗУЛЬТАТЫ АНАЛИЗА МАТРИЦЫ:\n")
            fo.write("1. Сумма в столбцах без отрицательных: {}\n".format(s1))
            fo.write("2. Мин. сумма модулей параллельных диагоналей: {}\n".format(s2))

        print("Результаты записаны в lab5_out.txt")

    except FileNotFoundError:
        print("Ошибка: Файл lab5_in.txt не найден.")


if __name__ == "__main__":
    main()