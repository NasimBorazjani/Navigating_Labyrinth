
cities = ['F', 'I', 'C', 'G', 'N', 'L', 'X', 'Q', 'U', 'R', 'O', 'B']
distances = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
]

def get_nearest_city(current_city, visited_cities):
    min_distance = float('inf')
    nearest_city = None
    for i in range(len(cities)):
        if distances[current_city][i] == 1 and cities[i] not in visited_cities:
            if distances[current_city][i] < min_distance:
                min_distance = distances[current_city][i]
                nearest_city = i
    return nearest_city

path = ['G']
visited_cities = ['G']
for _ in range(2):
    for city in ['O', 'R']:
        nearest_city = get_nearest_city(cities.index(city), visited_cities)
        path.append(cities[nearest_city])
        visited_cities.append(cities[nearest_city])
        path.append(city)

path.append('G')
print(path)
