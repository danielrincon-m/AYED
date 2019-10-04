from sys import stdin


def test_solution():
    inputs = [0, 1, 2]
    expected_outputs = ['-', [[1]], [[2, 2, 2], [2, 1, 2], [2, 2, 2]]]
    number_of_cases = len(inputs)
    for case in range(number_of_cases):
        output = solve(inputs[case] * 2 - 1)
        if output == expected_outputs[case]:
            print('Caso ' + str(case + 1) + ' válido')
        else:
            print('Caso ' + str(case + 1) + ' inválido')


def calculate_matrix_value(x, y, center):
    return max(abs(x - center), abs(y - center)) + 1


def print_solution(solution_matrix, size_of_matrix):
    if size_of_matrix == -1:
        print(solution_matrix)
        return
    for x in range(size_of_matrix):
        for y in range(size_of_matrix):
            if y != size_of_matrix - 1:
                print(solution_matrix[x][y], end='\t')
            else:
                print(solution_matrix[x][y], end='\n')


def solve(size_of_matrix):
    # 2. Verificar entrada
    if size_of_matrix == -1:
        return '-'
    # 4. Construir matriz de ceros
    solution_matrix = [[0 for x in range(size_of_matrix)] for y in range(size_of_matrix)]
    # 5. Encontrar el centro de la matriz
    center_coord = size_of_matrix // 2
    # 6. Recorrer la matriz
    for x in range(size_of_matrix):
        for y in range(size_of_matrix):
            # 6.Encontrar la distancia al centro, sumarle 1 y escribirla en la matriz
            solution_matrix[x][y] = calculate_matrix_value(x, y, center_coord)
    # 7. Imprimir la respuesta
    return solution_matrix


def get_input():
    # 1. Leer entrada
    n = int(stdin.readline().strip())
    # 3. Calcular el tamaño de la matriz
    size_of_matrix = n * 2 - 1
    return size_of_matrix


def main():
    size_of_matrix = get_input()
    solution_matrix = solve(size_of_matrix)
    print_solution(solution_matrix, size_of_matrix)


main()
#test_solution()
