# 04. Connect Areas in a Matrix
class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def create_matrix(rows):
    for _ in range(rows):
        matrix.append(list(input()))


def find_info(rows, cols, areas):
    for row in range(rows):
        for col in range(cols):
            size = explore_area(row, col, matrix)

            if size == 0:
                continue

            areas.append(Area(row, col, size))


def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'

    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result


def print_result(areas):
    result = []
    result.append(f'Total areas found: {len(areas)}')

    for index, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
        result.append(f'Area #{index + 1} at ({area.row}, {area.col}), size: {area.size}')

    print(*result, sep='\n')


rows = int(input())
cols = int(input())

matrix = []
areas = []

create_matrix(rows)

find_info(rows, cols, areas)

print_result(areas)
