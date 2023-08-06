# Шейкерная сортировка O(n^2)

# проходимся по массиву с двух сторон,
# последовательно сравнивая текущий элемент правым или левым и
# меняя местами элементы расположенные в неправильном порядке

mas = [9, 6, 0, -190, 4500, -0.5, 8]

for l in range(len(mas)//2):
    for i in range(len(mas) - l - 1):
        begin = i
        end = len(mas) - 1 - i
        if mas[begin] > mas[begin + 1]:
            mas[begin], mas[begin + 1] = mas[begin + 1], mas[begin]
        if mas[end] < mas[end - 1]:
            mas[end], mas[end - 1] = mas[end - 1], mas[end]
print(mas)
