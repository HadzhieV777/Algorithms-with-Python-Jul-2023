# 01. Maze Explorer
from collections import deque


def shortest_path_in_maze(maze):
    n = len(maze)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Find starting point (S) and destination point (E)
    start = None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
                break
        if start:
            break

    # Validate position
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] != '#'

    queue = deque([(start[0], start[1], 0)])
    visited = set(start)

    while queue:
        x, y, steps = queue.popleft()
        if maze[x][y] == 'E':
            return steps

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, steps + 1))
                visited.add((new_x, new_y))

    return -1


n = int(input())
maze = []
for _ in range(n):
    row = input().strip()
    maze.append(row)

result = shortest_path_in_maze(maze)

if result != -1:
    print(result)
