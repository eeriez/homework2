def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

matrix = get_matrix(5, 5, 'a')
print(matrix)

#Сначала не так поняла задание, написала функцию, которая только выводит в консоль что-то похожее на матрицу.
#Удалять было жалко, пусть лежит уже
def print_matrix(n, m, value):
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        print(row)

print_matrix(3, 6, 'ooo')
