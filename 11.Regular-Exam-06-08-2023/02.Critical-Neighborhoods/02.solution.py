# 2. Critical Neighborhoods
from collections import deque

def find_shortest_path(start_city, end_city, roads, closed_roads):
    graph = {}

    for road in roads:
        city1, city2, distance = road

        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}

        graph[city1][city2] = distance
        graph[city2][city1] = distance 

    closed_set = set(tuple(closed_road.split("-")) for closed_road in closed_roads.split(","))

    queue = deque([(start_city, [start_city])])
    shortest_distance = float('inf')
    shortest_path = None

    while queue:
        current_city, path = queue.popleft()

        if current_city == end_city:
            total_distance = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = path

        for neighbor, _ in graph[current_city].items():
            if neighbor not in path and (current_city, neighbor) not in closed_set and (neighbor, current_city) not in closed_set:
                queue.append((neighbor, path + [neighbor]))

    if shortest_path:
        return " - ".join(shortest_path), shortest_distance

    return None, None

r = int(input())
roads = []
for i in range(r):
    road = input().split(" - ")
    roads.append((road[0], road[1], int(road[2])))

closed_roads = input()
start_city = input()
end_city = input()

path, total_distance = find_shortest_path(start_city, end_city, roads, closed_roads)
print(path)
print(total_distance)
