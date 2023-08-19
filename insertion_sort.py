# Шейкерная вставками O(n^2)

# проходимся по массиву,
# последовательно выбарая элементам правильный индекс в отсортированном до текущего элемента массиве
# хорошо работатет на почти отсортированных массивах

mas = [9, 6, 0, -190, 4500, -0.5, 8]

for i in range(1, len(mas)):
    new_ind = i
    while (mas[i] < mas[new_ind - 1] and new_ind > 0):
        new_ind -= 1
    if new_ind != i:
        mas[i], mas[new_ind] = mas[new_ind], mas[i]
    print(mas)

print(mas)
