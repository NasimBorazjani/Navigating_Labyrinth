
# Adjacency matrix
adjacency_matrix = [
    "0000001000000",
    "0000110001001",
    "0000001000000",
    "0110000001001",
    "0000111000000",
    "1000000001000",
    "1000001001100",
    "1011000100100",
    "1000000100000",
    "0001100000001",
    "0011000000010",
    "0111000001000",
    "0110000000011",
]

# Convert adjacency matrix into dictionary
graph = {city: [] for city in 'SEDYFBHOUIQZJ'}
for i, row in enumerate(adjacency_matrix):
    for j, col in enumerate(row):
        if col == '1':
            graph[chr(i + ord('A'))].append(chr(j + ord('A')))

# Recursive function for depth-first search
def dfs(city, cities_left, path, visited_count):
    path.append(city)
    if city in cities_left:
        cities_left.remove(city)
        if city in ['B', 'H']:
            if visited_count[city] == 1:
                for next_city in graph[city]:
                    if next_city in cities_left:
                        result = dfs(next_city, cities_left, path, visited_count)
                        if result:
                            return result
                path.pop()
                cities_left.append(city)
        else:
            for next_city in graph[city]:
                if next_city in cities_left:
                    result = dfs(next_city, cities_left, path, visited_count)
                    if result:
                        return result
    elif city == 'O':
        visited_count['B'] += 1
        visited_count['H'] += 1
        for next_city in graph[city]:
            if next_city in cities_left:
                result = dfs(next_city, cities_left, path, visited_count)
                if result:
                    return result
    path.pop()
    return path if not cities_left else None

# List of cities left to visit
cities_left = [city for city in graph if city not in ['O', 'B', 'H']]

# Count of visited destination cities
visited_count = {'B': 0, 'H': 0}

# Start the depth-first search
result = dfs('O', cities_left, [], visited_count)

# Print the solution
print(result)
