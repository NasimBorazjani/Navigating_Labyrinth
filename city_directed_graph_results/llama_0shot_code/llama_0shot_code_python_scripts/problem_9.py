
import itertools

# Adjacency matrix
matrix = [
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
]

# Create a dictionary to represent the map
map = {letter: [] for letter in 'ABCDEFGHI'}
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == 1:
            map[chr(i + ord('A'))].append(chr(j + ord('A')))

# Function to calculate the total weight of a path
def total_weight(path):
    return sum(matrix[ord(path[i]) - ord('A')][ord(path[i + 1]) - ord('A')] for i in range(len(path) - 1))

# Generate all possible paths
start_city = 'C'
path_start = [start_city]
path_end = ['F', 'W']
path_middle = list(map.keys() - set(path_start) - set(path_end))

all_paths = [path_start + list(p) + path_end for p in itertools.permutations(path_middle, len(path_middle))]

# Find the shortest path
shortest_path = min(all_paths, key=total_weight)

print(shortest_path)
