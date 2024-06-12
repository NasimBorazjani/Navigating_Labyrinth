
cities = ['O', 'M', 'Y', 'J', 'Z', 'V', 'K', 'F', 'X', 'L', 'R']
distances = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
]

def get_nearest_city(current_city, visited_cities):
    min_distance = float('inf')
    nearest_city = None
    for i in range(len(cities)):
        if distances[current_city][i] > 0 and cities[i] not in visited_cities:
            if distances[current_city][i] < min_distance:
                min_distance = distances[current_city][i]
                nearest_city = i
    return nearest_city

path = ['M']
visited_cities = set()
current_city = 0  # Index of city 'M'

# Visit each city twice
for i in range(2):
    for city in cities:
        if city not in visited_cities:
            for _ in range(2):
                nearest_city = get_nearest_city(current_city, visited_cities)
                path.append(cities[nearest_city])
                visited_cities.add(cities[nearest_city])
                current_city = nearest_city

# Return to the starting city
path.append('M')

print(path)
