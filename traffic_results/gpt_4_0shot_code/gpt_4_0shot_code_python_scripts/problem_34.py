
import heapq

def a_star_search(city_map, start, end):
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        (cost, current, path) = heapq.heappop(heap)
        if current in visited:
            continue
        if current == end and set(map(lambda x: x[0]//3, path)) == {0, 1, 2}:
            return path
        visited.add(current)
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_position = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_position[0] < len(city_map) and
                0 <= next_position[1] < len(city_map[0]) and
                city_map[next_position[0]][next_position[1]] != 'x'):
                next_cost = cost + city_map[next_position[0]][next_position[1]]
                heapq.heappush(heap, (next_cost, next_position, path + [next_position]))

city_map = [
    [12, 11, 14, 10, 2, 11, 13, 16, 3, 'x', 12],
    [10, 9, 'x', 8, 'x', 'x', 1, 16, 11, 'x', 15],
    [1, 18, 1, 'x', 'x', 'x', 'x', 'x', 12, 9, 'x'],
    [1, 14, 15, 10, 7, 15, 17, 10, 15, 15, 6],
    [18, 11, 'x', 'x', 'x', 15, 'x', 'x', 1, 1, 'x'],
    [14, 'x', 'x', 'x', 18, 14, 16, 7, 'x', 1, 'x'],
    [11, 15, 'x', 'x', 15, 3, 11, 13, 'x', 'x', 'x'],
    [5, 'x', 'x', 'x', 'x', 'x', 15, 'x', 6, 'x', 'x'],
    [12, 11, 7, 2, 11, 'x', 10, 2, 17, 'x', 'x'],
    [7, 'x', 'x', 'x', 4, 'x', 4, 'x', 'x', 5, 'x'],
    ['x', 19, 10, 7, 'x', 2, 3, 9, 2, 6, 'x']
]

start = (7, 0)
end = (2, 9)
print(a_star_search(city_map, start, end))
