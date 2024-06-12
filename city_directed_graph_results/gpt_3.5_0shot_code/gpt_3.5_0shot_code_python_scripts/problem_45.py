
import itertools

# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

# Define the cities
cities = ['Z', 'H', 'M', 'P', 'B', 'I', 'E', 'L', 'Q', 'Y', 'V', 'C']

# Initialize variables
start_city = 'C'
end_cities = ['M', 'Q']
min_time = float('inf')
min_path = None

# Generate all permutations of visiting M and Q twice
for perm in itertools.permutations(end_cities):
    for i in range(1, len(cities)):
        path = [start_city] + list(perm) + [start_city]
        time = 0
        valid_path = True
        for j in range(len(path) - 1):
            start_idx = cities.index(path[j])
            end_idx = cities.index(path[j+1])
            if adjacency_matrix[start_idx][end_idx] == 0:
                valid_path = False
                break
            time += 1
        if valid_path and time < min_time:
            min_time = time
            min_path = path

print(min_path)
